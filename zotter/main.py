import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel  # <--- ADDED THIS IMPORT
from .model import load_notes, save_notes, Note 

app = typer.Typer()
console = Console()

@app.command()
def add(title: str, content: str, category: str = "General"):
    """
    Add a new note. Usage: zotter add "Title" "Body" --category Work
    """
    notes = load_notes()
    new_note = Note(title, content, category)
    
    # Store as dictionary (JSON serializable)
    notes.append(new_note.__dict__) 
    save_notes(notes)
    
    console.print(f"[bold green]Success![/bold green] Note '{title}' added.")

@app.command()
def list():
    """
    List all notes in a pretty table.
    """
    notes = load_notes()
    
    if not notes:
        console.print("[red]No notes found. Add one first![/red]")
        return

    # Create a Rich Table
    table = Table(title="My Notes")
    table.add_column("Index", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Category", style="blue")
    table.add_column("Title", style="green")

    for idx, note in enumerate(notes):
        table.add_row(str(idx + 1), note['date'], note['category'], note['title'])

    console.print(table)

@app.command()
def view(index: int):   # <--- ADDED THIS COMMAND
    """
    View the full content of a note by its index.
    """
    notes = load_notes()
    
    # Adjust for 0-based indexing
    real_index = index - 1

    if 0 <= real_index < len(notes):
        note = notes[real_index]
        
        # Print the Category and Date
        console.print(f"[bold blue]{note['category']}[/bold blue] | [magenta]{note['date']}[/magenta]")
        
        # Print the Content in a Panel
        console.print(Panel(note['content'], title=f"[bold green]{note['title']}[/bold green]"))
    else:
        console.print(f"[bold red]Error:[/bold red] Note {index} not found.")

@app.command()
def delete(index: int):
    """
    Delete a note by its index (as shown in the list command).
    """
    notes = load_notes()
    
    # Adjust for 0-based indexing vs 1-based user input
    real_index = index - 1

    if 0 <= real_index < len(notes):
        removed = notes.pop(real_index)
        save_notes(notes)
        console.print(f"[bold red]Deleted:[/bold red] {removed['title']}")
    else:
        console.print(f"[bold red]Error:[/bold red] Index {index} not found.")

@app.command()
def search(query: str):
    """
    Search notes by keyword (Title or Content).
    """
    notes = load_notes()
    results = []

    # Filter notes (case-insensitive)
    for note in notes:
        if query.lower() in note['title'].lower() or query.lower() in note['content'].lower():
            results.append(note)

    if not results:
        console.print(f"[red]No matches found for '{query}'[/red]")
        return

    # Display results
    table = Table(title=f"Search Results for '{query}'")
    table.add_column("Index", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Category", style="blue")
    table.add_column("Title", style="green")

    # Note: We must find the ORIGINAL index so the user can delete it later
    for note in results:
        # We find the index of this note in the original full list
        original_index = notes.index(note) 
        table.add_row(str(original_index + 1), note['date'], note['category'], note['title'])

    console.print(table)
    
if __name__ == "__main__":
    app()