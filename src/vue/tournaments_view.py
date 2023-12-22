class TournamentView:

    @classmethod
    def get_tournament_info(cls):
        return {
            "name": input("Nom du tournoi: "),
            "place": input("Lieu du tournoi: ")
        }

    @classmethod
    def display_tournament(cls, _tournament):
        print(f"Date de début : {_tournament.start_date} \n")
        print(f"Nom du tournoi: {_tournament.name}")
        print(f"Lieu du tournoi: {_tournament.place}")
        print(f"Nombre de rondes: {_tournament.nb_rounds}")
        print("\n\nMENU:\n")

        if not _tournament.players:
            print("1. Ajouter des joueurs")
            return input("Choix: ")

        print("h: home \n")

        return input("Choix: ")

    @classmethod
    def list_tournaments(cls, tournaments):
        print("Liste des tournois")

        print("Nom\t\tLieu\t\tDate de début\t\tNombre de rounds")

        for tournament in tournaments:
            print(f"{tournament.name}\t{tournament.place}\t\t{tournament.start_date}\t{tournament.nb_rounds}")

            print("\n\nMENU:\n")

        return input("sélectionner un tournoi par son nom:")

    @classmethod
    def tournament_not_found(cls, tournament_name):
        print(f"Le tournoi {tournament_name} n'existe pas")

        return input("Appuyez sur une touche pour continuer")

    @classmethod
    def add_players(cls, players):
        print("Liste des joueurs")

        print("id\t\t\tnom\t\t\tprenom\t\t\tdate de naissance")

        for player in players:
            print(f"{player.id} {player.nom} {player.prenom} {player.date_naissance}")

        selected_players = []

        for i in range(3):
            player_id = input("sélectionner un joueur par son numéro d'identification:")
            player = next(p for p in players if p.id == player_id)
            selected_players.append(player)

        return selected_players
