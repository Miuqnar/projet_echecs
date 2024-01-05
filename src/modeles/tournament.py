import random
from datetime import datetime

from src.modeles.match import Match
from src.modeles.player import Player
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
        self.rounds = []
        self.players = []
        self.director_remark = ""

    def start_tournament(self):
        # Vérifier s'il y a assez de joueurs pour commencer le tournoi
        if len(self.players) < 2:
            print("Il n'y a pas assez de joueurs pour commencer le tournoi.")
            return
        print(self.rounds)
        # Mélanger les joueurs pour le premier tour
        random.shuffle(self.players)

        first_round = Round(name="Tour 1")

        match1 = Match(self.players[0], self.players[1])
        first_round.matches.append(match1)

        match2 = Match(self.players[2], self.players[3])
        first_round.matches.append(match2)

        # match3 = Match(self.players[4], self.players[5])
        # first_round.matches.append(match3)
        #
        # match4 = Match(self.players[6], self.players[7])
        # first_round.matches.append(match4)

        self.rounds.append(first_round)



    @property
    def current_round(self):
        if not self.rounds:
            return None
        return self.rounds[-1]

    def start_next_round(self):
        # Vérifier si le nombre maximal de tours est atteint
        if self.current_round > self.nb_rounds:
            print("Le tournoi est terminé.")
            return

        # Génère les paires pour le prochain round
        new_round = Round(f"Round {self.current_round}")
        used_players = set()

        for i in range(0, len(self.players), 2):

            player1 = self.players[i]
            player2 = self.players[i + 1] if i + 1 < len(self.players) else None

            # Vérifie si les joueurs ont déjà joué l'un contre l'autre
            while player2 and (player1, player2) in used_players:
                i += 2
                player2 = self.players[i + 1] if i + 1 < len(self.players) else None

            if player2:
                used_players.add((player1, player2))
                used_players.add((player2, player1))

            new_round.add_match(player1, player2)

        # Ajoute le round à la liste des rounds du tournoi
        self.rounds.append(new_round)

        # self.current_round += 1

    def match_exists(self, player1, player2):
        for r in self.rounds:
            for match in r.matches:
                if (match.player1 == player1 and match.player2 == player2) or (
                        match.player1 == player2 and match.player2 == player1):
                    return True
        return False

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


if __name__ == '__main__':
    player_1 = Player(id="1", name="Doe", surname="John", birth_date="01/01/1990")
    player_2 = Player(id="2", name="Doe", surname="Jane", birth_date="01/01/1990")
    player_3 = Player(id="3", name="Doe", surname="Jack", birth_date="01/01/1990")
    player_4 = Player(id="4", name="Doe", surname="Jill", birth_date="01/01/1990")

    tournament = Tournament("Echecs", "Paris")
    tournament.players = [player_1, player_2, player_3, player_4]

    tournament.start_tournament()


