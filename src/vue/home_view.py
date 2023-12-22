class HomeView:
    # Interface utilisateur pour la gestion des tournois

    @classmethod
    def home_page(cls):
        print("MENU TOURNOI")
        print("1. Créer un tournoi")
        print("2. Résumé du tournoi")
        print("3. Gestion des joueurs")
        print("4. Sortir")

        return input("Choisissez une option:")
