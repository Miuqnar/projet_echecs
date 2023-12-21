class HomeView:
    # Interface utilisateur pour la gestion des tournois

    @staticmethod
    def prin_menu():
        print("MENU TOURNOI")
        list_menu = [
            "Céer un tournoi",
            "Résumé du tournoi",
            "Créer un joueur",
            "Sortir"
        ]
        print("Choisissez parmi les 5 options suivantes:")
        for i, menu_item in enumerate(list_menu, 1):
            print(f"{i}: {menu_item}")

    @classmethod
    def choice_list(cls):
        HomeView.prin_menu()
        return input("Choisissez parmi les options suivantes: ")



