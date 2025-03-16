from parser import extract_cells
from writer import write_python_script , write_readme_md

code_cells, markdown_cells = extract_cells("C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\input\\sample_notebook.ipynb")

output_dir = "C:\\Users\\Hp\\Desktop\\projects\\NBForge\\examples\\output\\sample_notebook"
write_python_script(code_cells , output_dir , "src.py")
write_readme_md(markdown_cells , output_dir , "readme.md")