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
        """
        Initialise le premier tour du tournoi
        en mélangeant aléatoirement les joueurs inscrits.
        """

        if len(self.players) < 2:
            print("Il n'y a pas assez de joueurs pour commencer le tournoi.")
            return

        # Mélanger les joueurs pour le premier tour
        random.shuffle(self.players)

        first_round = Round(name="Tour 1")

        # Ajouter les matchs au premier round
        for i in range(0, len(self.players), 2):
            match = Match(self.players[i], self.players[i + 1])
            first_round.matches.append(match)

        self.rounds.append(first_round)

    @property
    def current_round(self):
        """Renvoie la ronde actuelle du tournoi."""

        if not self.rounds:
            return None
        return self.rounds[-1]

    def start_next_round(self):
        """Démarre la prochaine ronde du tournoi."""

        if len(self.rounds) >= self.nb_rounds:
            print("Le tournoi est déjà terminé.")
            return

        self.players_score()

        new_round = Round(f"Tour {len(self.rounds) + 1}")

        pairs = self.generate_pairs()

        for pair in pairs:
            new_round.add_match(pair[0], pair[1])

        self.rounds.append(new_round)

    def generate_pairs(self):
        """Génère les paires de joueurs pour la prochaine ronde."""

        players_sorted = sorted(self.players,
                                key=lambda x: x.points, reverse=True)
        pairs = []

        for i in range(0, len(players_sorted), 2):
            player1 = players_sorted[i]
            player2 = players_sorted[i + 1] if i + 1 < len(players_sorted) else None

            while player2 and self.match_exists(player1, player2):
                i += 1
                player2 = players_sorted[i] if i < len(players_sorted) else None

            if player2:
                pairs.append((player1, player2))

        return pairs

    def match_exists(self, player1, player2):
        """
        Vérifie si un match entre deux joueurs a
        déjà eu lieu dans les rondes précédentes.
        """

        for r in self.rounds:
            for match in r.matches:
                if (match.player1 == player1 and match.player2 == player2) or (
                        match.player1 == player2 and match.player2 == player1):
                    return True
        return False

    def players_score(self):
        """
        Calcule et met à jour les points des
        joueurs en fonction des résultats des matchs.
        """

        for player in self.players:
            player.points = 0

        for round_obj in self.rounds:
            for match in round_obj.matches:
                match.player1.points += match.score_player1
                match.player2.points += match.score_player2

        players_score = sorted(
            [{"player": player, "score": player.points}
             for player in self.players],
            key=lambda k: k["score"], reverse=True
        )

        return players_score

    def serialize(self):
        """
        Convertit les données du tournoi en
        un dictionnaire JSON serializable.
        """

        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "nb_rounds": self.nb_rounds,
            "rounds": [round_obj.serialize() for round_obj in self.rounds],
            "players": [player.serialize() for player in self.players],
            "director_remark": self.director_remark,
        }

    @classmethod
    def deserialize(cls, data):
        """
        Creation d'une instance de la classe
        Tournament à partir des données désérialisées.
        """

        instance = cls(
            name=data["name"],
            place=data["place"]
        )

        instance.start_date = data["start_date"]
        instance.end_date = data["end_date"]
        instance.nb_rounds = data["nb_rounds"]
        instance.director_remark = data["director_remark"]

        # Désérialiser les joueurs
        instance.players = [Player.deserialize(player_data)
                            for player_data in data["players"]]

        # Désérialiser les rounds
        instance.rounds = [Round.deserialize(round_data)
                           for round_data in data["rounds"]]

        # Appeler start_tournament pour
        # mettre à jour correctement current_round
        instance.start_tournament()

        return instance
