from src.modeles.player import Joueur


class Match:
    def __init__(self, joueur1: Joueur, joueur2: Joueur):
        # Initialisation des attributs du match
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = 0
        self.score_joueur2 = 0

    def definir_le_joueur_gagnant1(self):
        self.score_joueur1 = 1
        self.score_joueur2 = 0
        self.joueur1.points += 1

    def definir_le_joueur_gagnant2(self):
        self.score_joueur1 = 0
        self.score_joueur2 = 1
        self.joueur2.points += 1

    def set_draw(self):
        self.score_joueur1 = 0.5
        self.score_joueur2 = 0.5
        self.joueur1.points += 0.5
        self.joueur2.points += 0.5
