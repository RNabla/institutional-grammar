import click
from pathlib import Path

import igannotator.main
# import igrelations.main

@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
def console_entry(input_file, output_dir):
    input_file_path = Path(input_file)
    output_dir_path = Path(output_dir)
    if output_dir_path.exists() and not output_dir_path.is_dir():
        raise IOError(f'{putput_dir} does exist and is not a directory')
    output_dir_path.mkdir(parents=True,exist_ok=True)
    output_mae_file = input_file_path.stem + '_mae.xml'
    igannotator.main.annotate_file(input_file, str(output_dir_path / output_mae_file))
    pass
