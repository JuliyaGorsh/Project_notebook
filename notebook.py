

notebook = []

def get_notebook() -> list:
    global notebook
    return notebook

def set_notebook(new_notebook: list):
    global notebook
    notebook = new_notebook