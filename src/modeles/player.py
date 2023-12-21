class Joueur:
    id_echecs = 0

    def __init__(self, nom, prenom, date_naissance):
        # Initialisation des attributs du joueur et incrementer l'id joueur
        Joueur.id_echecs += 1
        self.id = Joueur.id_echecs

        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.points = 0
