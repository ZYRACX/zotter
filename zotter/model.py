import json
from pathlib import Path
from datetime import datetime

# Define where the notes will be saved
NOTES_FILE = Path.home() / ".zotter.json"

class Note:
    def __init__(self, title, content, category="General"):
        self.title = title
        self.content = content
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

def load_notes():
    if not NOTES_FILE.exists():
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes_list):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes_list, f, indent=4)