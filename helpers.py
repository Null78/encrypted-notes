from rich.table import Table
from rich.padding import Padding
import aes

def setup_table():
    table = Table()
    table.add_column("ID")
    table.add_column("Note", style="magenta")
    table.add_column("Created At", style="green")
    table.add_column("Updated At", style="green")
    return table

def print_one(note, console, password = None):
    table = setup_table()
    content = decrypt_note(note, password)
    table.add_row(str(note[0]), str(content), str(note[3]), str(note[4]))
    console.print(Padding(table, (0, 0, 1, 0)))

def print_many(notes, console, password = None):
    table = setup_table()
    for note in notes:
        content = decrypt_note(note, password)
        table.add_row(str(note[0]), content, str(note[3]), str(note[4]))
    console.print(Padding(table, (2, 1)))

def decrypt_note(note, password):
    if not password:
        return "*** Encrypted Note ***"
    try:
        return aes.decrypt(password, note[2], note[1]).decode()
    except UnicodeError:
        return "*** Encrypted Note ***"