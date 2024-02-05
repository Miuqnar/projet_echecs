import json

from src.constants.constant import DATA_DIR
from src.modeles.player import Player
from src.modeles.tournament import Tournament


class TournamentDataManager:
    @classmethod
    def save_data_to_json(cls, data_store):
        """Enregistre les données des tournois au format JSON."""

        for tournament in data_store['tournaments']:
            tournament_filename = DATA_DIR / f"{tournament.name}.json"

            with open(tournament_filename, 'w') as json_file:
                json.dump(tournament.serialize(), json_file, indent=4)

    @classmethod
    def save_player_to_json(cls, player):
        """Sauvegarde les données spécifiques (nom ou prénom)
        d'un joueur dans un fichier JSON."""
        players_file_path = DATA_DIR / "../players.json"
        player_data = cls.load_players()

        # Mettre à jour uniquement le nom ou le prénom du joueur
        for player_id in player_data:
            if player_id == player.id:
                data = player_data[player_id]
                if player.name:
                    data.name = player.name
                if player.surname:
                    data.surname = player.surname

        with open(players_file_path, 'w') as f:
            # Reconvertir la structure de données en
            # dictionnaire avant de l'enregistrer
            player_data_dict = [player_data[player_id].serialize()
                                for player_id in player_data]
            # Enregistrer le dictionnaire sérialisé dans
            # le fichier JSON avec une mise en forme indentée
            json.dump(player_data_dict, f, indent=4)

    @classmethod
    def load_players(cls):
        """Charge les données des joueurs à partir d'un
        fichier JSON et retourne un dictionnaire."""
        players = {}
        players_file_path = DATA_DIR / "../players.json"
        with open(players_file_path, "r") as f:
            players_data = json.load(f)
            # Parcourir les données des joueurs et les désérialiser
            for player_data in players_data:
                player = Player.deserialize(player_data)
                players[player.id] = player
        return players

    @classmethod
    def load_tournaments(cls, players):
        """Charge les données des tournois à partir des fichiers JSON."""
        loaded_tournaments = []
        for tournament_file in DATA_DIR.glob("*.json"):
            with open(tournament_file, 'r') as json_file:
                tournament_data = json.load(json_file)
                loaded_tournaments.append(
                    Tournament.deserialize(tournament_data, players)
                )
        return loaded_tournaments
