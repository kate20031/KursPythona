import json
from functools import reduce


def remove_output_cells(notebook):
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            cell['outputs'] = []


def remove_code_helper(notebook, i):
    curr_cell = notebook['cells'][i]
    prev_cell = notebook['cells'][i - 1]
    if (curr_cell['cell_type'] == 'code' and prev_cell['cell_type'] == 'markdown'
            and "### Ćwiczenie" in prev_cell['source'][0]):
        notebook['cells'].pop(i)
    return notebook


def remove_code(notebook):
    return reduce(remove_code_helper, range(len(notebook['cells']) - 1, 0, -1), notebook)


if __name__ == "__main__":
    input_file = "/home/acer/Pobrane/funkcyjny_s.ipynb"

    with open(input_file, 'r') as f:
        notebook = json.load(f)

    remove_output_cells(notebook)
    notebook = remove_code(notebook)

    output_file = input_file.replace('.ipynb', '.czysty.ipynb')

    with open(output_file, 'w') as f:
        json.dump(notebook, f)
