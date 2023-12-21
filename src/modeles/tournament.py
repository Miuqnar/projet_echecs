from datetime import datetime


class Tournament:
    def __init__(self, name, place):
        # initialisation des attribus du tournoi
        self.name = name
        self.place = place
        current_date = datetime.now()
        self.start_date = current_date.strftime('%d-%m-%Y %H:%M:%S')
        self.end_date = None
        self.nb_rounds = 4
        self.current_round = 1
        self.rounds = []
        self.players = []
        self.director_remark = ""

    def serialize(self):
        # Convertit les attributs en un dictionnaire pour faciliter la manipulation des données
        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "nb_rounds": self.nb_rounds,
            "current_round": self.current_round,
            "rounds": self.rounds,
            "players_save": self.players,
            "director_remark": self.director_remark,
        }

    def generer_paires(self, tournoi):
        #  générer les paires de chaque tour
        pass
