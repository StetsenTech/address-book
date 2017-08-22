"""Modules handles setting up pytest configurations"""
import pytest


@pytest.fixture(scope="module")
def invalid_entries():
    invalid = [
    ]

    return invalid

@pytest.fixture(scope="module")
def valid_entries():
    valid = [
    ]

    return valid

@pytest.fixture(scope="module")
def mix_entries(valid_entries, invalid_entries):
    mix = valid_entries + invalid_entries
    
    return mix