import json
from pathlib import Path
from datetime import datetime

# Define where the notes and trash will be saved
NOTES_FILE = Path.home() / ".zotter.json"
TRASH_FILE = Path.home() / ".zotter_trash.json"  # <--- NEW FILE

class Note:
    def __init__(self, title, content, category="General"):
        self.title = title
        self.content = content
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

def load_data(filepath):
    """Generic helper to load data from any JSON file"""
    if not filepath.exists():
        return []
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(filepath, data):
    """Generic helper to save data to any JSON file"""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

# --- Helper Wrappers ---
def load_notes():
    return load_data(NOTES_FILE)

def save_notes(notes_list):
    save_data(NOTES_FILE, notes_list)

def load_trash():
    return load_data(TRASH_FILE)

def save_trash(trash_list):
    save_data(TRASH_FILE, trash_list)