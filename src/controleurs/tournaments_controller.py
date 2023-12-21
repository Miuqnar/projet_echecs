from src.modeles.tournament import Tournament
from src.vue.tournaments_view import TournamentView


class TournamentController:
    # créer un nouveau tournament

    @classmethod
    def display_list(cls, data_store, route_params=None):
        # Vérifier s'il y a des tournois dans le data_store
        # tournaments = data_store.get("tournament", [])

        tournament = TournamentView.show_options_for_returning_home(data_store["tournament"])
        if tournament.lower() == "h":
            return "home", None
        raise ValueError(f"Appuyez sur h pour revenir à la page d'accueil.")

    @classmethod
    def create_tournament(cls, data_store, route_params=None):
        tournament_data = TournamentView.get_tournament_info()
        tournament = Tournament(tournament_data['name'],
                                tournament_data['place'])

        data_store["tournament"].append(tournament)

        return "display_tournament", None

    @classmethod
    def save_tournament(cls):
        pass
