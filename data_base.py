

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