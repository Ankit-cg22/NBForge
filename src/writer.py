def write_python_script(code_cells, output_dir , output_file):
    output_path = f"{output_dir}/{output_file}"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Auto-generated from Jupyter Notebook\n\n")
        for idx, code in enumerate(code_cells):
            f.write(code + "\n\n")

def write_readme_md(markdown_cells , output_dir , output_file):
    output_path = f"{output_dir}/{output_file}"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("### Note : Auto-generated from Jupyter Notebook\n\n")
        for idx, md in enumerate(markdown_cells):
            f.write(md + "\n\n")