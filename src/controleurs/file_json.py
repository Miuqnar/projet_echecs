import json

from src.constants.constant import DATA_DIR
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
    def load_data_from_json(cls):
        """Charge les données des tournois à partir des fichiers JSON."""
        loaded_tournaments = []

        for tournament_file in DATA_DIR.glob("tournament_*.json"):
            with open(tournament_file, 'r') as json_file:
                tournament_data = json.load(json_file)
                loaded_tournaments.append(
                    Tournament.deserialize(tournament_data)
                )

        return {"tournaments": loaded_tournaments, "players": []}
