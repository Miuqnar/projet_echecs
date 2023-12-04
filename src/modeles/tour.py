from datetime import datetime

from src.modeles.match import Match


class Tour:
    def __init__(self, nom, date_debut):
        # Initialisation des attributs du tour
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = None
        self.matchs = []

    def terminer_tour(self):
        # Mettre à jour la date de fin du tour
        self.date_fin = datetime.now()

    def ajouter_match(self, joueur1, joueur2):
        # Ajouter un match à la liste des matchs
        self.matchs.append(Match(joueur1, joueur2))
