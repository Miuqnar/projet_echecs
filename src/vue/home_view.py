class HomeView:

    @classmethod
    def home_page(cls):
        """
        Affiche le menu principal et
        demande à l'utilisateur de faire un choix.
        """

        print("MENU TOURNOI")
        print("1. Créer un tournoi")
        print("2. Résumé du tournoi")
        print("3. Sortir")

        return input("Choisissez une option:")
