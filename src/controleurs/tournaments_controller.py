from src.modeles.tournament import Tournament
from src.vue.tournaments_view import TournamentView


# Non-Breaking Space(NBSP)
class TournamentController:

    @classmethod
    def display_tournament(cls, data_store, tournament_name=None):
        """
        Affiche les détails d'un tournoi
        et gère les actions de l'utilisateur.
        """

        try:
            # Rechercher le tournoi par nom dans la liste des tournois
            tournament = next(t for t in data_store["tournaments"] if t.name == tournament_name)
        except StopIteration:
            TournamentView.tournament_not_found(tournament_name)

            return "home", None

        # Afficher les options pour le tournoi
        choice = TournamentView.display_tournament(tournament)

        if choice == "h":
            return "home", None
        elif choice == "1":
            return "add_players", tournament_name
        elif choice == "2":
            tournament.start_tournament()
        elif choice == "3":
            return "enter_results", tournament_name
        elif choice == "4":
            tournament.start_next_round()
        else:
            print("Choix invalide")

        return "display_tournament", tournament.name

    @classmethod
    def create_tournament(cls, data_store, tournament_name=None):
        """
        Crée un nouveau tournoi en demandant
        des informations à l'utilisateur.
        """

        tournament_data = TournamentView.get_tournament_info()
        tournament = Tournament(tournament_data['name'],
                                tournament_data['place'])

        data_store["tournaments"].append(tournament)

        return "display_tournament", tournament_data['name']

    @classmethod
    def add_players(cls, data_store, route_params=None):
        """Ajoute des joueurs à un tournoi."""

        tournament = next(t for t in data_store["tournaments"] if t.name == route_params)

        # Ajouter des joueurs au tournoi à partir de la vue
        players = TournamentView.add_players(data_store["players"])
        tournament.players = players

        return "display_tournament", tournament.name

    @classmethod
    def list_tournament(cls, data_store, route_params=None):
        """
        Affiche la liste des tournois et
        demande le choix de l'utilisateur.
        """

        choice = TournamentView.list_tournaments(data_store["tournaments"])

        if choice == "h":
            return "home", None

        return "display_tournament", choice

    @classmethod
    def enter_results(cls, data_store, route_params=None):
        """Saisit les résultats des matches pour un tournoi."""

        tournament = next(t for t in data_store["tournaments"] if t.name == route_params)

        TournamentView.display_round(tournament.current_round, TournamentView.display_matches)

        round_choice = TournamentView.enter_results_menu(tournament.current_round.matches)

        while round_choice.lower() != "h":
            if round_choice.isdigit():
                match_number = int(round_choice)
                selected_match = tournament.current_round.matches[match_number - 1]
                match_result = TournamentView.enter_results_choice(selected_match)

                # Logique de scoring de la classe Match
                selected_match.assign_points(match_result)

                TournamentView.display_round(tournament.current_round, TournamentView.display_matches)

                # Vérifier si c'est le dernier match du tour
                if tournament.current_round.has_finished():
                    # Retourner automatiquement à la page display_tournament
                    return "display_tournament", tournament.name

                round_choice = TournamentView.enter_results_menu(tournament.current_round.matches)

        # Retourner à la page display_tournament après la fin de la boucle
        return "display_tournament", tournament.name
