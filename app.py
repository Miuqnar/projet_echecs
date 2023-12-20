import os
import subprocess as sp

from src.controleurs.home_controller import HomeController
from src.controleurs.tournaments_controller import TournamentController
from src.vue.tournaments_view import TournamentView


class App:
    ROUTES_MAPPING = {
        'home': HomeController.home_controller,
        'list_tournament': TournamentController.create_tournament,
        'display_tournament': TournamentController.display_list
    }

    def __init__(self) -> None:
        self.current_route = 'home'
        self.route_params = None
        self.data_store = {'tournament': []}
        self.exit_flag = False

    def run(self):
        while not self.exit_flag:
            # sp.call('clear', shell=True)
            os.system('clear' if os.name == 'posix' else 'cls')
            current_controller_method = self.ROUTES_MAPPING[self.current_route]

            next_route, next_params = current_controller_method(
                self.data_store, self.route_params
            )

            self.current_route = next_route
            self.route_params = next_params

            if next_params == "exit":
                self.exit_flag = True


if __name__ == '__main__':
    app = App()
    app.run()
