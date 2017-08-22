import json

import click

from address_book.components.entry import EntryComponent

@click.command()
@click.option('--input_file', '-i', default="data.in",
              type=click.Path(exists=True),
              help="Path to data file for input")
@click.option('--output_file', '-o', default="result.out",
              type=click.Path(exists=False),
              help="Path to output file")
def run_address_book(input_file, output_file):
    """Starts processing the address book"""
    with open(input_file, mode='r') as data_in:
        entry_input = data_in.readlines()

    entry_component = EntryComponent()
    result = entry_component.create_entry(entry_input, sort=True)

    with open(output_file, 'w+') as result_out:
        result_out.write(result)

if __name__ == '__main__':
    run_address_book()
