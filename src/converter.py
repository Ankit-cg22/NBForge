from parser import extract_cells
from writer import write_to_file
from chains import Chains 
import json 

code_cells, markdown_cells = extract_cells("C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\input\\sample_notebook.ipynb")

output_dir = "C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\output\\sample_notebook"
chains = Chains()

try :
    res = chains.get_file_structure(code_cells , markdown_cells)
    for obj in res :
        file_name = obj['fileName']
        file_content = obj['fileContent']
        write_to_file(output_dir , file_name , file_content)
except Exception as e:
    print("error occured \n" , e)

'''
[
    {
        "fileName": "README.md",
        "fileContent": "# Sample Jupyter Notebook\nThis is a test notebook for conversion."
    },
    {
        "fileName": "greet.py",
        "fileContent": "# Function: greet\n# This function takes a name and returns a greeting message.\n\ndef greet(name):\n    return f\"Hello, {name}!\""
    },
    {
        "fileName": "main.py",
        "fileContent": "import numpy as np\nimport pandas as pd\nfrom greet import greet\n\ndata = {'A': [1, 2, 3], 'B': [4, 5, 6]}\ndf = pd.DataFrame(data)\nname = \"Alice\"\nmessage = greet(name)\nprint(message)\nprint(df)"
    }
]
'''