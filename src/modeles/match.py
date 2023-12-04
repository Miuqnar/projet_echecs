from src.modeles.joueur import Joueur


class Match:
    def __init__(self, joueur1: Joueur, joueur2: Joueur):
        # Initialisation des attributs du match
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score = None
