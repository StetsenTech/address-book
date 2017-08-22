"""Module that adds methods to help with processing input"""
import re

# Regex validators for file input
VALIDATION = re.compile((
    r'(?P<first>[\w. ]+)\s'
    r'(?P<last>\w+),\s'
    r'(?P<phone>(\d{3}\s\d{3}\s\d{4}|\(\d{3}\)-\d{3}-\d{4})),\s'
    r'(?P<zip>\d{5}),\s'
))

def process_entries(entries):
    """Checks if entry data is valid

    Args:
        entries(list): List of personal information
        p_region(basestring): Region the phone is from
        p_format(basestring): Output format for phone number
    Returns:
        list, list: List of entry dictories and a list of invalid indices
    """
    valid_entries = [] # Tracks valid entries
    errors = [] # Tracks invalid entry indices

    for i, entry in enumerate(entries):
        # Check to see if entry is valid
        # If invalid, add index to list of invalid entries
        if VALIDATION.match(entry):
            entry_match = VALIDATION.match(entry)
        else:
            errors.append(i)
            continue

        # Check to see if entry is valid
        entry_dict = {
            "first_name": entry_match.group("first"),
            "last_name": entry_match.group("last"),
            "phone_number": entry_match.group("phone"),
            "color": entry_match.group("color"),
            "zipcode": entry_match.group("zip")
        }

        valid_entries.append(entry_dict)

    return valid_entries, errors
