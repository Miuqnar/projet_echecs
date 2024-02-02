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
    def load_players(cls):
        players = {}
        players_file_path = DATA_DIR / "../players.json"
        with open(players_file_path, "r") as f:
            players_data = json.load(f)
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



