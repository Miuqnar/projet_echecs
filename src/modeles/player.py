class Player:

    def __init__(self, id, name, surname, birth_date):
        # Initialisation des attributs du joueur et incrementer l'id joueur
        self.id = id
        self.name = name
        self.surname = surname
        # jour, mois, annee = map(int, birth_date.split('/'))
        self.birth_date = birth_date
        self.points = 0

