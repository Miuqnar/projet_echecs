import os
import subprocess as sp

from src.controleurs.home_controller import HomeController
from src.controleurs.tournaments_controller import TournamentController
from src.vue.tournaments_view import TournamentView


class App:
    # Creation des routes
    ROUTES_MAPPING = {
        'home': HomeController.home_controller,
        'list_tournament': TournamentController.create_tournament,
        'display_tournament': TournamentController.display_list
    }

    def __init__(self) -> None:
        # Initialisation de l'application avec des valeurs par défaut
        self.current_route = 'home'  # Route actuelle
        self.route_params = None  # Paramètres de la route
        self.data_store = {'tournament': []}
        self.exit_flag = False

    # Méthode pour exécuter l'application
    def run(self):
        while not self.exit_flag:
            # sp.call('clear', shell=True)
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
