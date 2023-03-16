

def list_to_str(notebook: list) -> str:
    str_notebook = ''
    for note in notebook:
        new_note = ';'.join(note)
        str_notebook += new_note + '\n'
    return str_notebook[:-1]