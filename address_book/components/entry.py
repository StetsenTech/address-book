"""Module hands methods that relate to address entries"""

from address_book.schemata.entry import EntrySchema
from address_book.utils.inputs import process_entries

class EntryComponent(object):
    """Class that handles address book entry methods"""

    def create_entry(self, data, sort=False, indent=4):
        """Generates an output based on given data

        Args:
            data(list): List of address_book entries
            sort(bool): Whether or not to sort result
            indent(int): Number of spaces for indent
        Returns:
            basestring: JSON converted dictionary from schema
        """
        entries, errors = process_entries(data)
       
        schema = EntrySchema()

        output = {
            "entries": entries,
            "errors": errors
        }

        return schema.dumps(output, sort_keys=sort, indent=indent).data
