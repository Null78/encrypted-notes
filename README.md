# Encrypted Notes CLI
This Python CLI tool allows you to manage your notes securely by encrypting them with AES encryption. You can create, read, update, and delete notes using this command-line interface.

## Features

- **Encryption**: Notes are encrypted using AES encryption with a provided password.
Create: Create new notes with content encrypted using the provided password.
- **Read**: View the contents of a specific note by providing its ID and the password used for encryption.
- **Update**: Modify the content of an existing note with new encrypted content.
- **Delete**: Delete a note by providing its ID and the password used for encryption.
- **List**: View all notes stored in the database, decrypting them with the provided password.

## Installation
Clone this repository to your local machine:

```sh
git clone https://github.com/Null78/encrypted-notes
```

Navigate to the project directory:
```sh
cd encrypted-notes
```

Install the dependencies:
```sh
pip install -r requirements.txt
```

## Usage
### Commands
- **All**: List all notes stored in the database.
```sh
python main.py all <password>
```

- **Get**: Retrieve the content of a specific note by providing its ID.
```sh
python main.py get <id> <password>
```
- **Create**: Create a new note with the provided content.
```sh
python main.py create "<content>" <password>
```

Update: Update the content of an existing note with new content.
```sh
python main.py update <id> "<new_content>" <password>
```

Delete: Delete a note by providing its ID.
```sh
python main.py delete <id> <password>
```

### Note
- Replace \<password> with your chosen password for encryption and decryption.
- Replace \<content> with the content of your note enclosed in double quotes.
- Replace \<id> with the ID of the note you want to retrieve, update, or delete.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or features you'd like to see added.