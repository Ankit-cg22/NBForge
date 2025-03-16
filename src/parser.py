import nbformat 
def extract_cells(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    code_cells = [cell['source'] for cell in nb.cells if cell.cell_type == 'code']
    markdown_cells = [cell['source'] for cell in nb.cells if cell.cell_type == 'markdown']

    return code_cells, markdown_cells