from src.vue.home_view import HomeView


class HomeController:
    @classmethod
    def home_controller(cls, data_store=None, route_params=None):
        choice = HomeView.choice_list()

        if choice == "1":
            next_action = 'list_tournament'

            return next_action, None




