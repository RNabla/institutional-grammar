import click

@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
def console_entry(input_file, output_dir):
    pass
