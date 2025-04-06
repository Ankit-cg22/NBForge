from parser import extract_blocks
from writer import write_to_file
from chains import Chains 
import json 

code_blocks, markdown_blocks , streamlit_desc_block , fastAPI_desc_block = extract_blocks("C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\input\\sample_data_processing_fastapi.ipynb")

output_dir = "C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\output\\sample_data_processing_fastapi"
chains = Chains()

try:
    res = chains.get_file_structure(code_blocks, markdown_blocks , streamlit_desc_block,fastAPI_desc_block)
    # Write the files
    for file in res:
        file_name = file['fileName']
        file_content = file['fileContent']
        write_to_file(output_dir , file_name , file_content)
    print("written files. ")
    print("Setup complete!")

except Exception as e:
    print(f"Error: {e}")
