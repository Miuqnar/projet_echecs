import os

from src.controleurs.file_json import TournamentDataManager
from src.controleurs.home_controller import HomeController
from src.controleurs.tournaments_controller import TournamentController
from src.modeles.player import Player
from src.modeles.tournament import Tournament


class App:
    ROUTES_MAPPING = {
        'home': HomeController.home_controller,
        'create_tournament': TournamentController.create_tournament,
        'display_tournament': TournamentController.display_tournament,
        'list_tournaments': TournamentController.list_tournament,
        'add_players': TournamentController.add_players,
        'enter_results': TournamentController.enter_results,
    }

    def __init__(self) -> None:
        """Initialisation de l'application"""

        self.current_route = 'home'  # Route actuelle
        self.route_params = None  # Paramètres de la route

        tournament1 = Tournament(name="Summer Paris", place="Paris")
        tournament2 = Tournament(name="Annual Lyon", place="Lyon")

        player1 = Player(
            id="1", name="Wick", surname="John", birth_date="01/01/1990"
        )
        player2 = Player(
            id="2", name="Doe", surname="Jane", birth_date="01/01/1990"
        )
        player3 = Player(
            id="3", name="Chan", surname="Jack", birth_date="01/01/1990"
        )
        player4 = Player(
            id="4", name="Chloe", surname="Jill", birth_date="01/01/1990"
        )
        player5 = Player(
            id="6", name="Potter", surname="Herry", birth_date="01/01/1990"
        )
        player6 = Player(
            id="5", name="Chris", surname="Nicola", birth_date="01/01/1990"
        )
        player7 = Player(
            id="7", name="Cris", surname="Ronaldo", birth_date="01/01/1990"
        )
        player8 = Player(
            id="8", name="smith", surname="Will", birth_date="01/01/1990"
        )

        players = TournamentDataManager.load_players()
        data = TournamentDataManager.load_tournaments(players)

        self.data_store = {'tournaments': data,
                           "players": players.values()}

        # self.data_store = data

        self.exit_flag = False

    def run(self):
        """Boucle principale de l'application."""

        while not self.exit_flag:
            os.system('clear' if os.name == 'posix' else 'cls')

            # Obtenir la méthode du contrôleur
            # actuel à partir du mapping des routes

            current_controller_method = self.ROUTES_MAPPING[self.current_route]

            # Chaque contrôleur devrait renvoyer deux choses :
            # - la prochaine route à afficher
            # - les paramètres nécessaires pour la prochaine route
            next_route, next_params = current_controller_method(
                self.data_store, self.route_params
            )

            # Définir la prochaine route et les paramètres d'entrée
            self.current_route = next_route
            self.route_params = next_params

            # Appel à save data to json après chaque modification importante
            TournamentDataManager.save_data_to_json(self.data_store)

            # Vérifier si la sortie de l'application est demandée
            if next_params == "exit":
                return self.exit_flag

        # Sauvegarder les données une dernière fois avant la sortie définitive
        TournamentDataManager.save_data_to_json(self.data_store)


if __name__ == '__main__':
    app = App()
    app.run()
