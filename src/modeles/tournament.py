import random
from datetime import datetime

from src.modeles.match import Match
from src.modeles.player import Player
from src.modeles.round import Round
from src.vue.tournaments_view import TournamentView


class Tournament:
    def __init__(self, name, place):
        # initialisation des attribus du tournoi
        self.name = name
        self.place = place
        current_date = datetime.now()
        self.start_date = current_date.strftime('%d-%m-%Y %H:%M:%S')
        self.end_date = None
        self.nb_rounds = 4
        self.rounds = []
        self.players = []
        self.director_remark = ""

    def start_tournament(self):
        # Vérifier s'il y a assez de joueurs pour commencer le tournoi
        if len(self.players) < 2:
            print("Il n'y a pas assez de joueurs pour commencer le tournoi.")
            return
        # Mélanger les joueurs pour le premier tour
        random.shuffle(self.players)

        first_round = Round(name="Tour 1")

        # Ajouter les matchs au premier round
        for i in range(0, len(self.players), 2):
            match = Match(self.players[i], self.players[i + 1])
            first_round.matches.append(match)

        self.rounds.append(first_round)

    @property
    def current_round(self):
        if not self.rounds:
            return None
        return self.rounds[-1]

    def start_next_round(self):
        # Vérifier si le tournoi est déjà terminé
        if len(self.rounds) >= self.nb_rounds:
            print("Le tournoi est déjà terminé.")
            return

        # Génère les paires pour le prochain round
        new_round = Round(f"Tour {len(self.rounds) + 1}")

        # Créer une liste de joueurs triés par score
        players_sorted = sorted(self.players, key=lambda player: player.points, reverse=True)

        # Génération des paires en évitant les matchs déjà joués
        pairs = []

        for i in range(0, len(players_sorted), 2):
            player1 = players_sorted[i]
            player2 = players_sorted[i + 1] if i + 1 < len(players_sorted) else None

            # Vérifier si le joueur a déjà joué contre l'autre joueur dans ce tournoi
            while player2 and self.match_exists(player1, player2):
                i += 1
                player2 = players_sorted[i] if i < len(players_sorted) else None

            # Exclure les joueurs avec la valeur None
            if player2:
                # Ajouter les joueurs associés
                pairs.append((player1, player2))

        # Ajout des matchs au tour
        for pair in pairs:
            new_round.add_match(pair[0], pair[1])

        self.rounds.append(new_round)

    def match_exists(self, player1, player2):
        for r in self.rounds:
            for match in r.matches:
                if (match.player1 == player1 and match.player2 == player2) or (
                        match.player1 == player2 and match.player2 == player1):
                    return True
        return False

    def serialize(self):
        # Convertit les attributs en un dictionnaire pour faciliter la manipulation des données
        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "nb_rounds": self.nb_rounds,
            "current_round": self.current_round,
            "rounds": self.rounds,
            "players": self.players,
            "director_remark": self.director_remark,
        }


# if __name__ == '__main__':
#     tournament = Tournament("echecs", "Paris")
#     tournament.start_next_round()
#     player_1 = Player(id="1", name="Doe", surname="John", birth_date="01/01/1990")
#     player_2 = Player(id="2", name="Doe", surname="Jane", birth_date="01/01/1990")
#     player_3 = Player(id="3", name="Doe", surname="Jack", birth_date="01/01/1990")
#     player_4 = Player(id="4", name="Doe", surname="Jill", birth_date="01/01/1990")
#
#     tournament = Tournament("Echecs", "Paris")
#     tournament.players = [player_1, player_2, player_3, player_4]
#
#     for i in range(tournament.nb_rounds):
#         round_name = f"Round {i + 1}"
#         new_round = Round(round_name)
#         tournament.rounds.append(new_round)
#
#     for current_round in tournament.rounds:
#         for i in range(0, len(tournament.players), 2):
#             player_1 = tournament.players[i]
#             player_2 = tournament.players[i + 1]
#             # print("player 1", player_1.surname)
#             # print("player 2", player_2.surname)
#             current_round.add_match(player_1, player_2)
#
#     for current_round in tournament.rounds:
#         print(current_round.name)
#         for match in current_round.matches:
#             print(match)
#             match.assign_points()
#
#     for player in tournament.players:
#         print(f"{player.surname} {player.points}")
