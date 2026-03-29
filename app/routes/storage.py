from pathlib import Path
import json

# Directory where data files are stored
DATA_DIR = Path("data")

# Full path to the JSON file that stores issues
DATA_FILE = DATA_DIR / "issues.json"


def load_data():
    # Check if the file exists before trying to open it
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read()

            # Avoid JSON parse error on empty files
            if content.strip():
                return json.loads(content)  # Convert JSON string → Python list

            # Return empty list if file doesn't exist or is empty
            return []


def save_data(data):
    # Create the data/ directory if it doesn't exist (no error if it does)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w") as f:
        # Convert Python object → JSON and write to file (indented for readability)
        json.dump(data, f, indent=2)