# Zotter 📝

**Zotter** is a lightning-fast, terminal-based note-taking tool built for developers who live in the command line. It allows you to capture thoughts, categorize ideas, and search your history without ever leaving your terminal.

Built with **Python**, **Typer**, and **Rich**.

---

## 📑 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Trash Management](#-trash-management)
- [Tech Stack](#-tech-stack)

---

## ✨ Features

* **Capture Ideas:** Quickly save titles and descriptions with categories.
* **Pretty Timeline:** View all notes in a beautifully formatted table.
* **Peek Mode:** Quickly view note content in a clean panel.
* **Search:** Instant fuzzy search across titles and content.
* **Safety Net:** Deleted notes go to a Trash bin and can be recovered.
* **Persistent Storage:** Data is saved locally in a hidden JSON file (`~/.zotter.json`).

---

## 🚀 Installation

### Prerequisites
* **Python 3.7+** (Required)
* **Git** (Optional, for easier updates)

### Option A: Using Git (Recommended)
*Best for keeping the app updated.*

1.  **Clone the repository**
    ```bash
    git clone https://github.com/starzooka/zotter.git
    cd zotter
    ```

2.  **Create a Virtual Environment**
    * **Windows:**
      ```powershell
      python -m venv venv
      .\venv\Scripts\activate
      ```
    * **Mac/Linux:**
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install the App**
    ```bash
    pip install --editable .
    ```

### Option B: Without Git (Manual Download)
*Best if you don't have Git installed.*

1. **Download the Code**
  * - Click the green **Code** button at the top of this page.
    - Select **Download ZIP**.
    - Extract the ZIP folder to your computer.

2. **Open Terminal**
    - Open your terminal or command prompt and navigate into the extracted folder.

3. **Install the App**

  **Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  pip install --editable .

```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install --editable .

```

### Option C: Global Install (Pipx) 🏆

*Best for running Zotter from ANY directory without activating environments.*

1. **Install pipx** (if you haven't already):
```bash
python -m pip install pipx
python -m pipx ensurepath

```


*(Restart your terminal after this step)*
2. **Install Zotter:**
```bash
# Navigate to the zotter folder first
pipx install .

```



---

## 📖 Usage Guide

Here is the complete command reference to master your workflow.

### ➕ Capture a Note

Create a new note. If you don't provide a category, it defaults to "General".

```bash
zotter add "Project Alpha" "Finish the API documentation by Friday" --category Work

```

### 📋 List Timeline

See a summary table of all your active notes.

```bash
zotter list

```

### 👁️ Peek at a Note

Take a quick look at the full content of a note using its ID.

```bash
zotter peek 1

```

### 🔍 Search

Find notes containing keywords in the Title or Body.

```bash
zotter search "API"

```

### 🗑️ Discard (Move to Trash)

Move a note to the Trash bin. It is **not** permanently deleted yet.

```bash
zotter delete 1

```

---

## ♻️ Trash Management

### View Trash

See notes you have discarded.

```bash
zotter trash

```

### Recover

Restore a note from the Trash back to your main timeline.

```bash
zotter recover 1

```

### Burn

Permanently destroy a specific note from the Trash. **This cannot be undone.**

```bash
zotter burn 1

```

### Incinerate

Permanently destroy **all** items in the Trash.

```bash
zotter incinerate

```

---

## 🛠️ Tech Stack

* **[Typer](https://typer.tiangolo.com/)**: For building the CLI commands.
* **[Rich](https://rich.readthedocs.io/)**: For beautiful terminal formatting (tables, colors, panels).
* **Python**: Core logic and JSON handling.

## 👤 Author

**STARZOOKA**

* GitHub: [https://github.com/starzooka](https://github.com/starzooka)

---

*Enjoy using Zotter!* 🚀

