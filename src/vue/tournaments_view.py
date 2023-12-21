class TournamentView:

    @classmethod
    def get_tournament_info(cls):
        try:
            return {
                "name": input("Nom du tournoi: "),
                "place": input("Lieu du tournoi: ")
            }
        except ValueError as e:
            print(f"ERREUR: {e}")
            return None

    @classmethod
    def display_tournament(cls, _tournament):
        print("Un nouveau tournoi a été créé")
        print(f"Date de début : {_tournament.start_date} \n")
        print(f"Nom du tournoi: {_tournament.name}")
        print(f"Lieu du tournoi: {_tournament.place}")
        print(f"Nombre de rondes: {_tournament.nb_rounds}")

    @classmethod
    def show_options_for_returning_home(cls, data_store):
        for tournament in data_store:
            TournamentView.display_tournament(tournament)

        print("h: home \n")
        choice = input("Choix: ")

        return choice



