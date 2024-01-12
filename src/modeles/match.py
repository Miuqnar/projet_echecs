class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def has_result(self):
        return self.score_player1 != 0 or self.score_player2 != 0

    # def define_winner(self):
    #     if self.score_player1 > self.score_player2:
    #         return self.player1
    #     elif self.score_player1 < self.score_player2:
    #         return self.player2
    #     else:
    #         return None

    def assign_points(self, match_result: int):
        """if match_result = 1 then player1 wins else: if match_result = 2 then player2 wins otherwise it's drow"""
        if match_result == 1:
            self.score_player1 = 1
        elif match_result == 2:
            self.score_player2 = 2
        else:
            self.score_player1 += 0.5
            self.score_player2 += 0.5


