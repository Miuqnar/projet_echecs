from datetime import datetime

from src.modeles.match import Match


class Round:
    def __init__(self, name):
        # Initialisation des attributs du tour
        self.name = name
        current_date = datetime.now()
        self.start_date = current_date.strftime('%d-%m-%Y %H:%M:%S')
        self.end_date = current_date.strftime('%d-%m-%Y %H:%M:%S')
        self.matches = []

    def has_finished(self):
        return all([match.has_result() for match in self.matches])

    def add_match(self, player1, player2):
        # Ajouter un match au tour
        match = Match(player1, player2)
        self.matches.append(match)


