import os

from src.controleurs.home_controller import HomeController
from src.controleurs.tournaments_controller import TournamentController
from src.modeles.player import Player
from src.modeles.tournament import Tournament


class App:
    # Creation des routes
    ROUTES_MAPPING = {
        'home': HomeController.home_controller,
        'create_tournament': TournamentController.create_tournament,
        'display_tournament': TournamentController.display_tournament,
        'list_tournaments': TournamentController.list_tournament,
        'add_players': TournamentController.add_players,
        'start_first_round': TournamentController.start_first_round,
    }

    def __init__(self) -> None:
        # Initialisation de l'application avec des valeurs par défaut
        self.current_route = 'home'  # Route actuelle
        self.route_params = None  # Paramètres de la route

        # TODO: delete
        tournament1 = Tournament(name="Summer Paris", place="Paris")
        tournament2 = Tournament(name="Annual Lyon", place="Lyon")

        player1 = Player(id="1", name="Doe", surname="John", birth_date="01/01/1990")
        player2 = Player(id="2", name="Doe", surname="Jane", birth_date="01/01/1990")
        player3 = Player(id="3", name="Doe", surname="Jack", birth_date="01/01/1990")
        player4 = Player(id="4", name="Doe", surname="Jill", birth_date="01/01/1990")
        player5 = Player(id="5", name="Doe", surname="John", birth_date="01/01/1990")
        player6 = Player(id="6", name="Doe", surname="Jane", birth_date="01/01/1990")
        player7 = Player(id="7", name="Doe", surname="Jack", birth_date="01/01/1990")
        player8 = Player(id="8", name="Doe", surname="Jill", birth_date="01/01/1990")

        # add 10 players

        self.data_store = {'tournaments': [tournament1, tournament2],
                           "players": [player1, player2, player3, player4, player5, player6, player7, player8]}

        self.exit_flag = False

    # Méthode pour exécuter l'application
    def run(self):
        while not self.exit_flag:
            # Nettoyer l'écran de la console (compatible avec différents systèmes d'exploitation)
            os.system('clear' if os.name == 'posix' else 'cls')

            # Obtenir la méthode du contrôleur actuel à partir du mapping des routes
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

            # Vérifier si la sortie de l'application est demandée
            if next_params == "exit":
                self.exit_flag = True


if __name__ == '__main__':
    app = App()
    app.run()
