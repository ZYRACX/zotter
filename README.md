```markdown
# Zotter 📝

**Zotter** is a lightning-fast, terminal-based note-taking tool built for developers who live in the command line. It allows you to capture thoughts, categorize ideas, and search your history without ever leaving your terminal.

Built with **Python**, **Typer**, and **Rich**.

## ✨ Features

* **Add Notes:** Quickly save titles and descriptions with categories.
* **Pretty Listing:** View all notes in a beautifully formatted table.
* **Read Mode:** View note content in a clean panel.
* **Search:** Instant fuzzy search across titles and content.
* **Persistent Storage:** Data is saved locally in a hidden JSON file (`~/.zotter.json`).

---

## 🚀 Installation

### Prerequisites
* Python 3.7+
* Git

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/zotter.git](https://github.com/YOUR_USERNAME/zotter.git)
cd zotter

```

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\activate

```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Install the App

```bash
pip install --editable .

```

### 4. Verify Installation

```bash
zotter --help

```

---

## 📖 Usage Guide

Here is the complete command reference to master your workflow.

### ➕ Add a Note

Create a new note. If you don't provide a category, it defaults to "General".

```bash
zotter add "Project Alpha" "Finish the API documentation by Friday" --category Work

```

### 📋 List All Notes

See a summary table of all your notes with their Index IDs.

```bash
zotter list

```

### 👁️ View a Note

Read the full content of a note using its Index ID (find the ID using the `list` command).

```bash
zotter view 1

```

### 🔍 Search

Find notes containing keywords in the Title or Body.

```bash
zotter search "API"

```

### 🗑️ Delete

Remove a note permanently by its ID.

```bash
zotter delete 1

```

---

## 🛠️ Tech Stack

* **[Typer](https://typer.tiangolo.com/)**: For building the CLI commands.
* **[Rich](https://rich.readthedocs.io/)**: For beautiful terminal formatting (tables, colors, panels).
* **Python**: Core logic and JSON handling.

## 👤 Author

**STARZOOKA**

* GitHub: https://github.com/starzooka

---

*Enjoy using Zotter!* 🚀

```
