class Player:

    def __init__(self, id, nom, prenom, date_naissance):
        # Initialisation des attributs du joueur et incrementer l'id joueur
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.points = 0
