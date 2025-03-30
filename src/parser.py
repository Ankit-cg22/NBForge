import nbformat 
from utils.constants import STREAMLIT_BLOCK_CONSTANT

def extract_blocks(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    code_blocks = [cell['source'] for cell in nb.cells if cell.cell_type == 'code']
    markdown_blocks = []
    streamlit_desc_block = None  

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            if is_streamlit_desc_block(cell['source']):
                streamlit_desc_block = cell['source']  
            else:
                markdown_blocks.append(cell['source'])  

    return code_blocks, markdown_blocks, streamlit_desc_block

def is_streamlit_desc_block(cell):
    """
    Checks if the first line of the given cell contains 'NBForge_Streamlit' (case insensitive).
    
    Args:
        cell (str): The content of a notebook cell.
    
    Returns:
        bool: True if the first line contains 'NBForge_Streamlit' (case insensitive), False otherwise.
    """
    lines = cell.strip().split("\n")
    streamlit_constant = STREAMLIT_BLOCK_CONSTANT.lower()
    return streamlit_constant in lines[0].lower() if lines else False