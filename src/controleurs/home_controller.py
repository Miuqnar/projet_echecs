from src.vue.home_view import HomeView


class HomeController:
    @classmethod
    def home_controller(cls, data_store=None, route_params=None):
        """Contrôleur de la page d'accueil,
        gérant les choix de l'utilisateur.
        """

        choice = HomeView.home_page()

        if choice == "1":
            return 'create_tournament', None
        elif choice == "2":
            return 'list_tournaments', None
        elif choice == "3":
            print("Programme terminé. Au revoir!")
            return 'home', 'exit'

        return "home", None
