import random
from datetime import datetime

from src.modeles.round import Round


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

    def start_tournament(self):
        # Vérifier s'il y a assez de joueurs pour commencer le tournoi
        if len(self.players) < 2:
            print("Il n'y a pas assez de joueurs pour commencer le tournoi.")
            return

        # Créer les rondes et les matchs
        for round_number in range(1, self.nb_rounds + 1):
            round_name = f"Round {round_number}"
            new_round = Round(round_name)

            # Mélanger les joueurs pour chaque tour
            random.shuffle(self.players)

            # Créer des matchs pour le tour
            for i in range(0, len(self.players), 2):
                player1 = self.players[i]
                player2 = self.players[i + 1]
                new_round.add_match(player1, player2)

            # Ajouter le tour au tournoi
            self.rounds.append(new_round)

        # Définir le current_round du tournoi à 1
        self.current_round = 1

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
            "players": self.players,
            "director_remark": self.director_remark,
        }

