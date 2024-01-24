class Player:
    """ Initialisation des attributs du joueur et initialisation des points à 0"""

    def __init__(self, id, name, surname, birth_date):
        self.id = id
        self.name = name
        self.surname = surname
        # jour, mois, annee = map(int, birth_date.split('/'))
        self.birth_date = birth_date
        self.points = 0

    def serialize(self):
        """Convertit les données du joueur en un dictionnaire JSON serializable."""

        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date,
            "points": self.points,
        }

    @classmethod
    def deserialize(cls, data):
        """Crée une instance de la classe Player à partir des données désérialisées."""

        instance = cls(
            id=data["id"],
            name=data["name"],
            surname=data["surname"],
            birth_date=data["birth_date"]
        )

        instance.points = data["points"]

        return instance
