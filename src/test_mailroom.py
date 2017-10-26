"""Tests for mailroom, program that generates thank you letters and reports."""

import pytest

from mailroom import DONOR_DICT

DONOR_NAMES = [
    ('list', '1'),
    ('Flerg Blergington', 'donate'),
    ('Chelsea Dole', 'donate')
]

DONOR_AMOUNT = [
    ('Anne Hathaway', '-50', 'donate'),
    ('Remy Mei', '0', 'donate'),
    ('Barack Obama', '100', 'initial'),
    ('Count Basie', '1000', 'initial'),
    ('Duke Ellington', '79223', 'initial')
]


def test_dictionary():
    """Testing that the dictionary is created."""
    from mailroom import DONOR_DICT
    assert type(DONOR_DICT) == dict


@pytest.mark.parametrize('name, result', DONOR_NAMES)
def test_ask_donor_name(name, result):
    """Testing that donor_name is correctly routed."""
    from mailroom import ask_donor_name
    if name == 'list':
        assert ask_donor_name(name) == '1'
    else:
        assert ask_donor_name(name) == 'donate'
        assert type(DONOR_DICT[name]) == list


@pytest.mark.parametrize('donor_name, donor_amount, result', DONOR_AMOUNT)
def test_ask_donation_amount(donor_name, donor_amount, result):
    """Testing that donor_amount is calculating/redirecting."""
    from mailroom import ask_donor_name
    from mailroom import ask_donation_amount
    if donor_name not in DONOR_DICT:
        assert ask_donor_name(donor_name) == 'donate'
    assert ask_donation_amount(donor_name, donor_amount) == result
