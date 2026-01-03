import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from .model import load_notes, save_notes, load_trash, save_trash, Note 

# Configure the main app with a description and disable the default sort order to keep our logical grouping
app = typer.Typer(
    help="[bold green]Zotter[/bold green]: A profound terminal-based note-taking assistant.\n\n"
         "Manage your thoughts, capture ideas, and keep your history clean.",
    rich_markup_mode="rich"
)
console = Console()

# --- ACTIVE NOTE COMMANDS ---

@app.command(rich_help_panel="Active Notes")
def add(title: str, content: str, category: str = "General"):
    """
    [bold]Capture[/bold] a new thought into your notebook.

    Format:
      zotter add TITLE CONTENT [--category CATEGORY]

    Examples:
      zotter add "Idea" "Build a CLI help system"
      zotter add "Meeting" "Discussed Q1 roadmap" --category Work

    Notes:
      • Use quotes for multi-word titles or content
      • Categories help organize notes
    """

    notes = load_notes()
    new_note = Note(title, content, category)
    notes.append(new_note.__dict__) 
    save_notes(notes)
    console.print(f"[bold green]Success![/bold green] Note '{title}' captured.")

@app.command(rich_help_panel="Active Notes")
def list():
    """
    [bold]View[/bold] all active notes in a structured table.

    Format:
      zotter list

    Example:
      zotter list

    Notes:
      • Notes are shown in the order they were added
      • Use the ID column for other commands like peek or delete
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

@app.command(rich_help_panel="Active Notes")
def peek(index: int):
    """
    [bold]Read[/bold] the full content of a specific note.

    Format:
      zotter peek INDEX

    Example:
      zotter peek 2

    Notes:
      • Index refers to the ID shown in `zotter list`
    """

    notes = load_notes()
    if 0 <= index - 1 < len(notes):
        note = notes[index - 1]
        console.print(f"[bold blue]{note['category']}[/bold blue] | [magenta]{note['date']}[/magenta]")
        console.print(Panel(note['content'], title=f"[bold green]{note['title']}[/bold green]"))
    else:
        console.print(f"[bold red]Error:[/bold red] Note {index} not found.")

@app.command(rich_help_panel="Active Notes")
def search(query: str):
    """
    [bold]Search[/bold] notes by keyword in title or content.

    Format:
      zotter search QUERY

    Examples:
      zotter search idea
      zotter search meeting

    Notes:
      • Search is case-insensitive
      • Matches both title and content
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

@app.command(rich_help_panel="Active Notes")
def delete(index: int):
    """
    [bold]Discard[/bold] a note by moving it to the Trash.

    Format:
      zotter delete INDEX

    Example:
      zotter delete 3

    Notes:
      • Deleted notes can be recovered later
      • Use `zotter trash` to view discarded notes
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

@app.command(rich_help_panel="Trash Management")
def trash():
    """
    [bold]Inspect[/bold] notes currently stored in the Trash.

    Format:
      zotter trash

    Example:
      zotter trash

    Notes:
      • Items here are not permanently deleted
      • You can recover or destroy them
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

@app.command(rich_help_panel="Trash Management")
def recover(index: int):
    """
    [bold]Restore[/bold] a discarded note back to active notes.

    Format:
      zotter recover INDEX

    Example:
      zotter recover 1

    Notes:
      • Index refers to the ID shown in `zotter trash`
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

@app.command(rich_help_panel="Trash Management")
def burn(index: int):
    """
    [bold]Permanently destroy[/bold] a single note from the Trash.

    Format:
      zotter burn INDEX

    Example:
      zotter burn 2

    Warning:
      • This action cannot be undone
    """

    trash = load_trash()
    real_index = index - 1

    if 0 <= real_index < len(trash):
        removed = trash.pop(real_index)
        save_trash(trash)
        console.print(f"[bold red]Permanently destroyed:[/bold red] {removed['title']}")
    else:
        console.print(f"[bold red]Error:[/bold red] Trash Item {index} not found.")

@app.command(rich_help_panel="Trash Management")
def incinerate():
    """
    [bold]Obliterate[/bold] all notes currently in the Trash.

    Format:
      zotter incinerate

    Example:
      zotter incinerate

    Warning:
      • This permanently deletes ALL trashed notes
      • You will be asked for confirmation
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

if __name__ == "__main__":
    app()