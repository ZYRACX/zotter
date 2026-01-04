# Zotter 📝

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey?style=for-the-badge)

**Zotter** is a lightning-fast, terminal-based note-taking tool built for developers who live in the command line. Capture thoughts, categorize ideas, and search your history without ever leaving your terminal.

Built with **Python**, **Typer**, and **Rich**.

---

## ✨ Features

* **⚡ Capture Ideas:** Instantly save titles and descriptions with custom categories.
* **🎨 Pretty Timeline:** View all notes in a beautifully formatted, color-coded table.
* **👁️ Peek Mode:** Read full note content in a clean, distraction-free panel.
* **🔍 Fuzzy Search:** Find any note instantly by keyword in the title or body.
* **🛡️ Safety Net:** Deleted notes move to a Trash bin first (recoverable).
* **🔥 Incinerator:** Permanently destroy specific notes or wipe the trash clean.
* **💾 Persistent Storage:** Data is saved locally in a hidden JSON file (`~/.zotter.json`).

---

## 🚀 Installation

### Prerequisites
* **Python 3.7+**
* **Git** (Optional)

### Option A: Using Git (Recommended)
*Best for keeping the app updated.*

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/starzooka/zotter.git](https://github.com/starzooka/zotter.git)
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

* **Download the Code**
    * Click the green **Code** button at the top of this page.
    * Select **Download ZIP**.
    * Extract the ZIP folder to your computer.

* **Open Terminal**
    * Open your terminal/command prompt and navigate into the extracted folder.

* **Install the App**
    * **Windows:**
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        pip install --editable .
        ```
    * **Mac/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        pip install --editable .
        ```

### Option C: Global Install (Pipx) 🏆
*Best for running Zotter from ANY directory without activating environments.*

1.  **Install pipx** (if you haven't already):
    ```bash
    pip install pipx
    pipx ensurepath
    ```
    *(Restart your terminal after this step)*

2.  **Install Zotter:**
    ```bash
    # Navigate to the zotter folder first
    pipx install .
    ```

---

## 📖 Usage Guide

Here is the command reference to master your workflow.

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

| Component | Purpose |
| --- | --- |
| **[Typer](https://typer.tiangolo.com/)** | CLI command construction and argument parsing. |
| **[Rich](https://rich.readthedocs.io/)** | Beautiful terminal formatting (tables, colors, panels). |
| **Python** | Core logic and JSON data handling. |

## 👤 Author

**STARZOOKA**

* GitHub: [https://github.com/starzooka](https://github.com/starzooka)

---

*Enjoy using Zotter!* 🚀
