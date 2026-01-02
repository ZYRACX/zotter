import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from .model import load_notes, save_notes, load_trash, save_trash, Note 

app = typer.Typer()
console = Console()

# --- ACTIVE NOTE COMMANDS ---

@app.command()
def add(title: str, content: str, category: str = "General"):
    """
    Add a new note.
    """
    notes = load_notes()
    new_note = Note(title, content, category)
    notes.append(new_note.__dict__) 
    save_notes(notes)
    console.print(f"[bold green]Success![/bold green] Note '{title}' captured.")

@app.command()
def list():
    """
    List all active notes.
    """
    notes = load_notes()
    if not notes:
        console.print("[dim]Your notebook is empty.[/dim]")
        return

    table = Table(title="Active Notes")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Category", style="blue")
    table.add_column("Title", style="green")

    for idx, note in enumerate(notes):
        table.add_row(str(idx + 1), note['date'], note['category'], note['title'])

    console.print(table)

@app.command()
def peek(index: int):
    """
    Take a quick peek at a specific note.
    """
    notes = load_notes()
    if 0 <= index - 1 < len(notes):
        note = notes[index - 1]
        console.print(f"[bold blue]{note['category']}[/bold blue] | [magenta]{note['date']}[/magenta]")
        console.print(Panel(note['content'], title=f"[bold green]{note['title']}[/bold green]"))
    else:
        console.print(f"[bold red]Error:[/bold red] Note {index} not found.")

@app.command()
def search(query: str):
    """
    Search notes by keyword.
    """
    notes = load_notes()
    results = []
    for note in notes:
        if query.lower() in note['title'].lower() or query.lower() in note['content'].lower():
            results.append(note)

    if not results:
        console.print(f"[red]No matches found for '{query}'[/red]")
        return

    table = Table(title=f"Search Results for '{query}'")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Category", style="blue")
    table.add_column("Title", style="green")

    for note in results:
        original_index = notes.index(note) 
        table.add_row(str(original_index + 1), note['date'], note['category'], note['title'])
    console.print(table)

@app.command()
def delete(index: int):
    """
    Move a note to the Trash (can be recovered later).
    """
    notes = load_notes()
    trash = load_trash()
    
    real_index = index - 1

    if 0 <= real_index < len(notes):
        removed_note = notes.pop(real_index)
        trash.append(removed_note)
        save_notes(notes)
        save_trash(trash)
        console.print(f"[bold yellow]Moved to Trash:[/bold yellow] {removed_note['title']}")
    else:
        console.print(f"[bold red]Error:[/bold red] Index {index} not found.")

# --- TRASH MANAGEMENT COMMANDS ---

@app.command()
def trash():
    """
    Show deleted notes in the Recycle Bin.
    """
    trash_items = load_trash()

    if not trash_items:
        console.print("[green]Trash is empty.[/green]")
        return

    table = Table(title="🗑️  Recycle Bin")
    table.add_column("ID", style="red", no_wrap=True)
    table.add_column("Date Deleted", style="dim")
    table.add_column("Title", style="dim")

    for idx, note in enumerate(trash_items):
        table.add_row(str(idx + 1), note['date'], note['title'])

    console.print(table)

@app.command()
def recover(index: int):
    """
    Recover a note from Trash back to the active list.
    """
    trash = load_trash()
    notes = load_notes()
    
    real_index = index - 1

    if 0 <= real_index < len(trash):
        recovered_note = trash.pop(real_index)
        notes.append(recovered_note)
        save_notes(notes)
        save_trash(trash)
        console.print(f"[bold green]Recovered:[/bold green] {recovered_note['title']}")
    else:
        console.print(f"[bold red]Error:[/bold red] Trash Item {index} not found.")

@app.command()
def burn(index: int):
    """
    Permanently destroy a note from the Trash.
    """
    trash = load_trash()
    real_index = index - 1

    if 0 <= real_index < len(trash):
        removed = trash.pop(real_index)
        save_trash(trash)
        console.print(f"[bold red]Permanently destroyed:[/bold red] {removed['title']}")
    else:
        console.print(f"[bold red]Error:[/bold red] Trash Item {index} not found.")

@app.command()
def incinerate():
    """
    Permanently destroy all items in the Trash.
    """
    trash = load_trash()
    
    if not trash:
        console.print("[dim]Trash is already empty.[/dim]")
        return

    # Safety confirmation
    delete_all = typer.confirm("Are you sure you want to incinerate all items in Trash? This action cannot be undone.")
    
    if not delete_all:
        console.print("Aborted.")
        return

    # Save an empty list to the trash file
    save_trash([])
    console.print("[bold red]All trash incinerated.[/bold red] 🔥")