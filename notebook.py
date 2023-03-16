

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