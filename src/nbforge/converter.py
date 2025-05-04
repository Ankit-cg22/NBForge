from nbforge.parser import extract_blocks
from nbforge.writer import write_to_file
from nbforge.chains import Chains 
import json 
import os 
from nbforge.logger import setup_logger

logger = setup_logger(__name__)

def convert_notebook(input_file_path, output_dir):
    """
    Converts a Jupyter notebook into a structured Python project by extracting code, markdown, and special description blocks, then generating files accordingly.

    Args:
        input_file_path (str): Path to the Jupyter notebook file.
        output_dir (str): Directory where the output files will be written.

    Returns:
        None
    """
    try:
        logger.info(f"Starting conversion from notebook to python project. Notebook path : {input_file_path} , output directory : {output_dir}.")
        output_dir_path = get_output_dir(input_file_path , output_dir)
        chains = Chains()
        code_blocks, markdown_blocks , streamlit_desc_block , fastAPI_desc_block = extract_blocks(input_file_path)
        res = chains.get_file_structure(code_blocks, markdown_blocks , streamlit_desc_block,fastAPI_desc_block)
        # Write the files
        for file in res:
            file_name = file['fileName']
            file_content = file['fileContent']
            write_to_file(output_dir_path , file_name , file_content)
    except Exception as e:
        logger.error(f"Error: {e}")

def get_output_dir(input_file_path , output_dir):
    """
    Generates the output directory path based on the notebook file name.

    Args:
        input_file_path (str): Path to the Jupyter notebook file.
        output_dir (str): Base output directory.

    Returns:
        str: Full path to the output directory named after the notebook (without extension).
    """
    output_dir_name = input_file_path.split('/')[-1].split('.')[0]
    return os.path.join(output_dir, output_dir_name)