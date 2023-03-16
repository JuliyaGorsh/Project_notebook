import view
from datetime import datetime as dt

notebook = []

def get_notebook() -> list:
    global notebook
    return notebook

def set_notebook(new_notebook: list):
    global notebook
    notebook = new_notebook

def add_note():
    global notebook
    note = view.input_new_note()
    notebook.append(note)

def remove_note():
    global notebook
    id = view.input_remove_note()
    confirm = input(f'Вы точно хотите удалить заметку "{notebook[id-1][1]}"? (y/n)')
    if confirm.lower() == 'y':
        del_note = notebook.pop(id-1)