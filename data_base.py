
import notebook as nb
path = r'notebook.csv'

def load_note() -> list:
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    nb.set_notebook(str_to_list(data))
    print('Блокнот загружен\n')

def save_note():
    global path
    ready_book = list_to_str(nb.get_notebook())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(ready_book)
    print('Блокнот сохранен\n')

def list_to_str(notebook: list) -> str:
    str_notebook = ''
    for note in notebook:
        new_note = ';'.join(note)
        str_notebook += new_note + '\n'
    return str_notebook[:-1]

def str_to_list(notebook: list) -> list:
    new_list = []
    for note in notebook:
       new_note = note.strip().split(';')
       new_list.append(new_note)
    return new_list