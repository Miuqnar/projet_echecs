class TournamentView:

    @classmethod
    def get_tournament_info(cls):
        return {
            "name": input("Nom du tournoi: "),
            "place": input("Lieu du tournoi: ")
        }

    @classmethod
    def display_tournament(cls, _tournament):
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
            print("2. Lancer le premier round")
        else:
            current_round = _tournament.current_round
            if current_round:
                print(f"3. Entrer les résultats du {current_round.name}")
            if current_round.has_finished():
                print("4. Lancer le prochain tour")

        print("h: home \n")
        return input("Choix: ")

    @classmethod
    def display_rounds(cls, rounds, display_matches_func):
        print("\nTours: ")
        for round_obj in rounds:
            print(f"\n {round_obj.name} ({round_obj.start_date})")
            if round_obj.matches:
                display_matches_func(round_obj.matches)
            else:
                print("   Aucun match pour le moment")

    @classmethod
    def enter_results_menu(cls, matches):
        print("\nOptions disponibles :")

        for i, match in enumerate(matches, 1):
            if not match.has_result():
                print(f"{i}. Entrer le résultat du match {i}")

        print("h. Accueil")
        return input("Choix: ")

    @classmethod
    def enter_results_choice(cls, match):
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
    def display_players(cls, players):
        if players:
            print("\nListe des joueurs:")
            print("id\tnom\tprenom\tdate de naissance")
            for player in players:
                print(f"{player.id}\t{player.name}\t{player.surname}\t{player.birth_date}")
        else:
            print("\nAucun joueur inscrit.")

    @classmethod
    def display_matches(cls, matches):
        for i, match in enumerate(matches, 1):
            player1_name = f"{match.player1.name} {match.player1.surname}"
            player2_name = f"{match.player2.name} {match.player2.surname}"

            winner = match.define_winner()
            if match.has_result():
                if winner:
                    result_status = f"{winner.name} {winner.surname} a gagné"
                else:
                    result_status = f"Match nul"
            else:
                result_status = "en attente de résultats"

            print(f"\t{i}: {player1_name} vs {player2_name} \t - {result_status}")

    @classmethod
    def add_players(cls, players):
        print("Liste des joueurs")

        print("id\tnom\tprenom\tdate de naissance")

        for player in players:
            print(f"{player.id}\t{player.name}\t{player.surname}\t{player.birth_date}")

        selected_players = []

        for i in range(2):
            player_id = input("Sélectionner un joueur par son numéro d'identification:")
            player = next(p for p in players if p.id == player_id)
            selected_players.append(player)

        return selected_players

    @classmethod
    def list_tournaments(cls, tournaments):
        print("Liste des tournois\n")

        print("Nom\t\tLieu\tDate de début\t\tNombre de rounds\n")

        for tournament in tournaments:
            print(f"{tournament.name}\t{tournament.place}\t{tournament.start_date}\t{tournament.nb_rounds}")

        print("\nMENU:\n")

        return input("Sélectionner un tournoi par son nom: ")

    @classmethod
    def tournament_not_found(cls, tournament_name):
        print(f"Le tournoi {tournament_name} n'existe pas")

        return input("Appuyez sur une touche pour continuer")
