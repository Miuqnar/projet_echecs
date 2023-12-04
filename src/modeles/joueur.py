class Joueur:
    def __init__(self, id_echecs, nom, prenom, date_naissance):
        # Initialisation des attributs du joueur
        self.id_echecs = id_echecs
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.points = 0