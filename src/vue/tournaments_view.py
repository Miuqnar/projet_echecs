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

        if _tournament.players:
            print("\nListe des joueurs:")
            print("id\tnom\tprenom\tdate de naissance")
            for player in _tournament.players:
                print(f"{player.id}\t{player.name}\t{player.surname}\t{player.birth_date}")
        else:
            print("\nAucun joueur inscrit.")

        print("\nListe des Tours:")
        for _round in _tournament.rounds:
            # Afficher les détails de chaque tour
            print(f"{_round.name} debut: {_round.start_date} - Fin: {_round.date_fin}")
            cls.display_matches(_round.matches)

        print("\n\nMENU:\n")

        if not _tournament.players:
            print("1. Ajouter des joueurs")
        elif not _tournament.rounds:
            print("2. Démarrer le premier tour")
        else:
            current_round = _tournament.current_round
            if current_round.is_finished:
                print("3. Démarrer le prochain tour")
            else:
                print("4. Entrez le resultat de match")
                match_id = int(input("Entrez l'id du match: "))
                select_match = current_round.matches[match_id - 1]
                if select_match.is_finished:
                    print("On a déjà un resultat")
                else:
                    print(f"A. {select_match.player1} a gagné")
                    print(f"B. {select_match.player2} a gagné")
                    print(f"C. {select_match.player1} {select_match.player2} égalité")
                    return input("Entrez le resultat"), select_match

        print("h: home \n")
        return input("Choix: ")

    @classmethod
    def display_matches(cls, matches):
        print("\nInformations sur le tour :")
        for i, match in enumerate(matches, 1):
            print(f"{i}: {match.player1.surname} vs {match.player2.surname}")

        # print("\nRésultats du tour :")
        # for match in matches:
        #     print(f" {match.player1.surname} {match.score_player1} - {match.score_player2} {match.player2.surname}")
        #
        # print("\nScore des joueurs :")
        # for match in matches:
        #     print(f" {match.player1.surname}: {match.player1.points} points")
        #     print(f" {match.player2.surname}: {match.player2.points} points")

    @classmethod
    def add_players(cls, players):
        print("Liste des joueurs")

        print("id\tnom\tprenom\tdate de naissance")

        for player in players:
            print(f"{player.id} {player.name} {player.surname} {player.birth_date}")

        selected_players = []

        for i in range(8):
            player_id = input("sélectionner un joueur par son numéro d'identification:")
            player = next(p for p in players if p.id == player_id)
            selected_players.append(player)

        return selected_players

    @classmethod
    def list_tournaments(cls, tournaments):
        print("Liste des tournois")

        print("Nom\t\tLieu\tDate de début\t\tNombre de rounds")

        for tournament in tournaments:
            print(f"{tournament.name}\t{tournament.place}\t{tournament.start_date}\t{tournament.nb_rounds}")

            print("\nMENU:\n")

        return input("sélectionner un tournoi par son nom:")

    @classmethod
    def tournament_not_found(cls, tournament_name):
        print(f"Le tournoi {tournament_name} n'existe pas")

        return input("Appuyez sur une touche pour continuer")
