"""Tests for mailroom, program that generates thank you letters and reports."""


def test_initial_prompt(path='testpoe.txt'):
    """Test that trigrammer outputs actual trigram text."""
    from mailroom import initial_prompt
    # test for main function here


def test_dictionary():
    from mailroom import DONOR_DICT
    assert type(DONOR_DICT) == dict
