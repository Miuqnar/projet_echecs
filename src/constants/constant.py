from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()
ROOT_DIR = SOURCE_FILE.parent.parent
DATA_DIR = ROOT_DIR / "data" / "tournaments"
DATA_DIR.mkdir(exist_ok=True, parents=True)

