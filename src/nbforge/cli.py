import click
from nbforge.converter import convert_notebook  

@click.group()
def cli():
    pass

@cli.command()
@click.argument('notebook_path')
@click.argument('output_directory')
def convert(notebook_path, output_directory):
    """Convert a Jupyter notebook to a structured Python project."""
    convert_notebook(notebook_path, output_directory)

def main():
    cli()
