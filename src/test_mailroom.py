"""Tests for mailroom, program that generates thank you letters and reports."""


def test_initial_prompt():
    """Test that trigrammer outputs actual trigram text."""
    from mailroom import main
    from mailroom import ask_donor_name
    from mailroom import ask_donation_amount
    from mailroom import create_donor_report
    # test for main function here


def test_dictionary():
    """Testing that the dictionary is created."""
    from mailroom import DONOR_DICT
    assert type(DONOR_DICT) == dict


def test_ask_donor_name():
    """Testing that donor_name is correctly routed."""
    from mailroom import ask_donor_name
    ask_donor_name()
