from src.modeles.tournament import Tournament
from src.vue.tournaments_view import TournamentView


class TournamentController:
    # créer un nouveau tournament

    @classmethod
    def display_tournament(cls, data_store, tournament_name=None):
        # Vérifier s'il y a des tournois dans le data_store

        try:
            tournament = next(t for t in data_store["tournaments"] if t.name == tournament_name)
        except StopIteration:
            TournamentView.tournament_not_found(tournament_name)

            return "home", None

        choice = TournamentView.display_tournament(tournament)

        if choice == "h":
            return "home", None
        elif choice == "1":
            return "add_players", tournament_name
        elif choice == "2":
            tournament.start_tournament()
        else:
            print("Choix invalide")

        return "display_tournament", tournament.name

    @classmethod
    def create_tournament(cls, data_store, tournament_name=None):
        tournament_data = TournamentView.get_tournament_info()
        tournament = Tournament(tournament_data['name'],
                                tournament_data['place'])

        data_store["tournaments"].append(tournament)

        return "display_tournament", tournament_data['name']

    @classmethod
    def add_players(cls, data_store, route_params=None):
        tournament = next(t for t in data_store["tournaments"] if t.name == route_params)

        players = TournamentView.add_players(data_store["players"])
        tournament.players = players

        return "display_tournament", tournament.name

    @classmethod
    def list_tournament(cls, data_store, route_params=None):
        choice = TournamentView.list_tournaments(data_store["tournaments"])

        if choice == "h":
            return "home", None

        return "display_tournament", choice
