class TournamentView:

    @classmethod
    def get_tournament_info(cls):
        """
        Obtient les informations d'un
        tournoi depuis l'utilisateur.
        """

        return {
            "name": input("Nom du tournoi: ").strip().title(),
            "place": input("Lieu du tournoi: ").strip().title()
        }

    @classmethod
    def display_tournament(cls, _tournament):
        """
        Affiche les détails d'un tournoi, y compris
        les joueurs, les rondes et les options disponibles.
        """

        print(f"Date de début: {_tournament.start_date} \n")
        print(f"Nom du tournoi: {_tournament.name}")
        print(f"Lieu du tournoi: {_tournament.place}")
        print(f"Nombre de rondes: {_tournament.nb_rounds}")

        cls.display_players(_tournament.players)
        cls.display_rounds(_tournament.rounds, cls.display_matches)

        print("\n\nMENU:\n")

        if not _tournament.players:
            print("1. Ajouter des joueurs")
        elif not _tournament.rounds:
            print("2. Lancer le premier tour")
        else:
            current_round = _tournament.current_round

            if not current_round.has_finished():
                print(f"3. Entrer les résultats du {current_round.name}")
            elif len(_tournament.rounds) < _tournament.nb_rounds:
                print("4. Lancer le prochain tour")
            else:
                print("Fin des tours")

        print("h: home \n")
        return input("Choix: ")

    @classmethod
    def display_players(cls, players):
        """Affiche la liste des joueurs."""

        if players:
            print("\nListe des joueurs:")
            print("id\tnom\tprenom\tdate de naissance")
            for player in players:
                # print(f"{player.id}\t{player.name}\t{player.surname}\t{player.birth_date}")
                print(f"{player.id}\t"
                      f"{player.name}\t"
                      f"{player.surname}\t"
                      f"{player.birth_date}")
        else:
            print("\nAucun joueur inscrit.")

    @classmethod
    def update_player_info(cls, player):
        print(f"1. Nom: {player.name}")
        print(f"2. Prénom: {player.surname} \n")
        # print("\nPour annuler, appuyez sur Entrée pour revenir à l'accueil")
        choice = input("Choix: ")

        if choice == '1':
            name_update = input("Nouveau nom: ")
            player.name = name_update
            return name_update
        elif choice == '2':
            surname_update = input("Nouveau prénom: ")
            player.surname = surname_update
            return surname_update

    @classmethod
    def select_player_option(cls, player):
        cls.display_players(player)

        while True:
            print("\n\n1. Mise à jour du joueur")
            print("h. home\n")
            choice = input("choix: ")

            if choice == 'h':
                break
            elif choice == '1':
                player_id = input("Saisir l'identifiant du joueur: ")
                return choice, player_id
            else:
                print("Choix invalide. Veuillez saisir une option valide.")

        return choice, None

    @classmethod
    def add_players(cls, players):
        """
        Demande à l'utilisateur
        de sélectionner des joueurs.
        """

        print("Liste des joueurs")

        print("id\tnom\tprenom\tdate de naissance")

        for player in players:
            # print(f"{player.id}\t{player.name}\t{player.surname}\t{player.birth_date}")
            print(
                f"{player.id}\t"
                f"{player.name}\t"
                f"{player.surname}\t"
                f"{player.birth_date}"
            )

        selected_players = []

        for _ in range(8):
            while True:
                try:
                    player_id = input("Sélectionner un joueur "
                                      "par son numéro d'identification:")
                    player = next(p for p in players if p.id == player_id)

                    if player_id not in [p.id for p in selected_players]:
                        selected_players.append(player)
                        break
                    else:
                        print("Ce joueur a déjà été sélectionné. "
                              "Veuillez choisir un autre joueur.")
                except StopIteration:
                    print("ID de joueur invalide. "
                          "Veuillez choisir un ID existant dans la liste.")

        return selected_players

    @classmethod
    def display_rounds(cls, rounds, display_matches_func):
        """Affiche les rondes et leurs matches."""

        print("\nTours: ")
        for round_obj in rounds:
            cls.display_round(round_obj, display_matches_func)

    @classmethod
    def display_round(cls, round_obj, display_matches_func):
        """Affiche les matches d'une ronde."""

        print(f"\n {round_obj.name} ({round_obj.start_date})")
        if round_obj.matches:
            display_matches_func(round_obj.matches)
        else:
            print("   Aucun match pour le moment")

    @classmethod
    def display_matches(cls, matches):
        """Affiche les matches."""

        for i, match in enumerate(matches, 1):
            player1_name = f"{match.player1.name} {match.player1.surname}"
            player2_name = f"{match.player2.name} {match.player2.surname}"

            winner = match.define_winner()
            if match.has_result():
                if winner:
                    result_status = f"{winner.name} {winner.surname} a gagné"
                else:
                    result_status = "Match nul"
            else:
                result_status = "en attente de résultats"

            print(f"\t{i}: {player1_name} vs {player2_name}\t-{result_status}")

    @classmethod
    def enter_results_menu(cls, matches):
        """Affiche le menu pour saisir les résultats des matches."""

        print("\nOptions disponibles :")

        for i, match in enumerate(matches, 1):
            if not match.has_result():
                print(f"{i}. Entrer le résultat du match {i}")

        print("h. home")
        return input("Choix: ")

    @classmethod
    def enter_results_choice(cls, match):
        """Demande à l'utilisateur de saisir le résultat d'un match."""

        while True:
            print("\nQui a gagné parmi ces joueur ?")
            print(f"1. {match.player1.name} {match.player1.surname} a gagné")
            print(f"2. {match.player2.name} {match.player2.surname} a gagné")
            print("3. Match nul")

            choice = input("Choix: ")

            if choice == "1":
                return 1
            elif choice == "2":
                return 2
            elif choice == "3":
                return 0  # Match nul
            else:
                print("Choix invalide. Veuillez choisir 1, 2 ou 3.")

    @classmethod
    def list_tournaments(cls, tournaments):
        """
        Affiche la liste des tournois et demande à
        l'utilisateur de sélectionner un tournoi.
        """

        print("Liste des tournois\n")

        print("Nom\t\tLieu\tDate de début\t\tNombre de rounds\n")

        for tournament in tournaments:
            # print(f"{tournament.name}\t{tournament.place}\t{tournament.start_date}\t{tournament.nb_rounds}")
            print(
                f"{tournament.name}\t"
                f"{tournament.place}\t"
                f"{tournament.start_date}\t"
                f"{tournament.nb_rounds}"
            )

        print("\nMENU:\n")
        print("\nh. home\n")

        return input("Sélectionner un tournoi par son nom: ").strip().title()

    @classmethod
    def tournament_not_found(cls, tournament_name):
        """Affiche un message indiquant qu'un tournoi n'a pas été trouvé."""

        print(f"Le tournoi {tournament_name} n'existe pas")

        return input("Appuyez sur une touche pour continuer")
