from parser import extract_cells
from writer import write_to_file
from chains import Chains 
import json 

code_cells, markdown_cells = extract_cells("C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\input\\sample_data_processing.ipynb")

output_dir = "C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\output\\sample_data_processing"
chains = Chains()

try:
    res = chains.get_file_structure(code_cells, markdown_cells)
    # Write the files
    print("writing files...")
    for file in res:
        file_name = file['fileName']
        file_content = file['fileContent']
        write_to_file(output_dir , file_name , file_content)
    print("written files. ")
    print("Setup complete!")

except Exception as e:
    print(f"Error: {e}")
