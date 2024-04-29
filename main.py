import typer
from rich.console import Console
from rich.padding import Padding
import db
import helpers
import aes

app = typer.Typer()
console = Console()


@app.command()
def all(password: str):
    notes = db.list()
    if notes:
        helpers.print_many(notes, console, password)
    else:
        console.print(Padding("No notes found", (2, 1), style="magenta"))


@app.command()
def get(id: int, password: str):
    note = db.get(id)
    helpers.print_one(note, console, password)


@app.command()
def create(content: str, password: str):
    cipher, iv = aes.encrypt(password, content)
    id = db.insert(cipher, iv)
    note = db.get(id);
    console.print(Padding("Note created successfully", (1, 1), style="green"))
    helpers.print_one(note, console, password)


@app.command()
def update(id: int, content: str, password: str):
    try:
        note = db.get(id)
        aes.decrypt(password, note[2], note[1]).decode()
    except:
        console.print(Padding("Bad Request", (1, 1), style="red"))
        raise typer.Exit()
    cipher, iv = aes.encrypt(password, content)
    db.update(id, cipher, iv)
    note = db.get(id)
    console.print(Padding("Note updated successfully", (1, 1), style="green"))
    helpers.print_one(note, console, password)


@app.command()
def delete(id: str, password: str):
    try:
        note = db.get(id)
        aes.decrypt(password, note[2], note[1]).decode()
    except:
        console.print(Padding("Bad Request", (1, 1), style="red"))
        raise typer.Exit()
    db.delete(id)
    console.print(Padding("Note deleted successfully", (1, 1), style="red"))


if __name__ == "__main__":
    app()