from nbforge.parser import extract_blocks
from nbforge.writer import write_to_file
from nbforge.chains import Chains 
import json 
import os 

def convert_notebook(input_file_path, output_dir):
    try:
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
        print(f"Error: {e}")

def get_output_dir(input_file_path , output_dir):
    output_dir_name = input_file_path.split('/')[-1].split('.')[0]
    return os.path.join(output_dir, output_dir_name)