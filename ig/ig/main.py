import click
from pathlib import Path

import igannotator.main
import igcogito.main
from igcogito.XML_parser.xls import MAEToXLSParser
# import igrelations.main

def setup_io(output_dir_path):
    if output_dir_path.exists() and not output_dir_path.is_dir():
        raise IOError(f'{output_dir} does exist and is not a directory')
    output_dir_path.mkdir(parents=True,exist_ok=True)

def get_output_filepath(input_file_path, output_dir_path, suffix):
    file_name = input_file_path.stem + suffix
    return output_dir_path / file_name


def create_mae_file(input_file_path, output_file_path):
    igannotator.main.annotate_file(str(input_file_path), str(output_file_path))

def create_xls_file(mae_file_path, output_file_path, mae_schema=None):
    if mae_schema == None:
        mae_schema = str(Path(__file__).parents[0] / 'mae_schema.xsd')
    print(mae_schema, mae_file_path)
    mae_parser = MAEToXLSParser(mae_schema, str(mae_file_path))
    mae_parser.parse_xml(str(output_file_path))

def create_csv_file(xls_file_path, output_file_path):
    with open(str(xls_file_path), 'rb') as f:
        igcogito.main.cogito(f, str(output_file_path))


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
@click.option("--mae_schema", type=click.Path())
def console_entry(input_file, output_dir, mae_schema):
    input_file_path = Path(input_file)
    output_dir_path = Path(output_dir)
    setup_io(output_dir_path)
    mae_file_path = get_output_filepath(input_file_path, output_dir_path, '_mae.xml')
    # create_mae_file(input_file_path, mae_file_path)
    xls_file_path = get_output_filepath(input_file_path, output_dir_path, '_excel.xls')
    create_xls_file(mae_file_path, xls_file_path, mae_schema=mae_schema)
    csv_file_path = get_output_filepath(input_file_path, output_dir_path, '_csv.csv')
    create_csv_file(xls_file_path, csv_file_path)
    
    pass
