from datetime import datetime

from src.modeles.tour import Tour


class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nb_tours=4, tour_actuel=1, remarque_directeur=""):
        # initialisation des attribus du tournoi
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tours = nb_tours
        self.tour_actuel = tour_actuel
        self.tours = []
        self.joueurs_enregistres = []
        self.remarque_directeur = remarque_directeur

    def ajouter_jouer(self, joueur):
        # Ajouter un joueur à la liste de joueur enregistré
        self.joueurs_enregistres.append(joueur)

    def commencer_tour(self):
        # Creation d'un nouvel objet Tour avec la date et l'heure actuelles
        tour_obj = Tour(f"Tour {self.tour_actuel}", datetime.now())
        self.tours.append(tour_obj)
        self.tour_actuel += 1
        return tour_obj
