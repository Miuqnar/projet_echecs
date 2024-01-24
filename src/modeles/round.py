from datetime import datetime

from src.modeles.match import Match


class Round:
    def __init__(self, name):
        """
        Initialisation d'une
        instance de la classe Round
        """

        self.name = name
        current_date = datetime.now()
        self.start_date = current_date.strftime('%d-%m-%Y %H:%M:%S')
        self.end_date = current_date.strftime('%d-%m-%Y %H:%M:%S')
        self.matches = []

    def has_finished(self):
        """
        Vérifie si tous les matchs
        dans le tour ont un résultat
        """

        return all([match.has_result() for match in self.matches])

    def add_match(self, player1, player2):
        """
        Ajouter un match au tour
        en créant une instance de la classe Match
        """

        match = Match(player1, player2)
        self.matches.append(match)

    def serialize(self):
        """
        Convertir l'objet Round en
        un dictionnaire pour la sérialisation
        """

        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [match.serialize() for match in self.matches],
        }

    @classmethod
    def deserialize(cls, data):
        """
        Méthode de classe pour désérialiser
         un dictionnaire en une instance de la classe Round
         """

        instance = cls(name=data["name"])

        instance.start_date = data["start_date"]
        instance.end_date = data["end_date"]

        # Désérialiser les matchs
        instance.matches = [Match.deserialize(match_data)
                            for match_data in data["matches"]]

        return instance
