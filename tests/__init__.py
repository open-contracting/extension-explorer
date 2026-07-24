import os
from pathlib import Path

os.environ["EXTENSION_EXPLORER_DATA_FILENAME"] = str(Path(__file__).resolve().parent / "fixtures" / "extensions.json")
