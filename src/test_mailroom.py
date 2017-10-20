"""Tests for mailroom, program that generates thank you letters and reports."""

DICT_KEYS = {
    'there blazed': ['forth', 'the'],
    'kept down': ['by', 'in'],
    'now got': ['up', 'some'],
    'A singular': ['change,'],
    'at first': ['had']
}


def test_initial_prompt(path='testpoe.txt'):
    """Test that trigrammer outputs actual trigram text."""
    from mailroom import initial_prompt
    # test for main function here


# def test_get_first_key_words(path='testpoe.txt'):
#     from trigram import get_first_key_words
#     from trigram import create_dict
#     created_dict = create_dict(path)
#     first_key = get_first_key_words(path, created_dict)
#     assert first_key in created_dict


# def test_trigrammer(n=50, path='testpoe.txt'):
#     from trigram import trigrammer
