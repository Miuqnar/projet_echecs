from src.modeles.player import Player


class Match:
    def __init__(self, player1, player2):
        """Initialisation des joueurs et des scores à 0 au début du match"""

        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def has_result(self):
        """Vérifie si le match a un résultat (score différent de 0 pour au moins un joueur)."""
        return self.score_player1 != 0 or self.score_player2 != 0

    def define_winner(self):
        """Détermine le gagnant du match en comparant les scores des joueurs."""
        if self.score_player1 > self.score_player2:
            return self.player1
        elif self.score_player1 < self.score_player2:
            return self.player2
        else:
            return None

    def assign_points(self, match_result: int):
        """if match_result = 1 then player1 wins else: if match_result = 1 then player2 wins otherwise it's drow"""
        """Attribue les points en fonction du résultat du match."""
        if match_result == 1:
            self.score_player1 = 1
        elif match_result == 2:
            self.score_player2 = 1
        else:
            self.score_player1 += 0.5
            self.score_player2 += 0.5

    def serialize(self):
        """Convertit les données du match en un dictionnaire JSON serializable."""
        return {
            "player1": self.player1.serialize(),
            "player2": self.player2.serialize(),
            "score_player1": self.score_player1,
            "score_player2": self.score_player2,
        }

    @classmethod
    def deserialize(cls, data):
        """Creation une instance de la classe Match à partir des données désérialisées."""
        instance = cls(player1=Player.deserialize(data["player1"]),
                       player2=Player.deserialize(data["player2"]))

        instance.score_player1 = data["score_player1"]
        instance.score_player2 = data["score_player2"]

        return instance
