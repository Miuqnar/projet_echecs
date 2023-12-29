class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def define_winner(self):
        if self.score_player1 > self.score_player2:
            return self.player1
        elif self.score_player1 < self.score_player2:
            return self.player2
        else:
            return None

    def assign_points(self):
        winner = self.define_winner()
        if winner:
            winner.points += 1

        else:
            self.player1.points += 0.5
            self.player2.points += 0.5

