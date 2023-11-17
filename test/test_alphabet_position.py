from src.alphabet_position.alphabet_position import (alphabet_position)


def test_funtuion_returns_string():
    result = alphabet_position('')
    assert isinstance(result, str)


def test_function_with_single_small_letter():
    result = alphabet_position('a')
    expected = '1'
    assert result == expected
    result = alphabet_position('h')
    expected = '8'
    assert result == expected
    result = alphabet_position('t')
    expected = '20'
    assert result == expected
    result = alphabet_position('z')
    expected = '26'
    assert result == expected


def test_function_with_single_capital_letter():
    result = alphabet_position('A')
    expected = '1'
    assert result == expected
    result = alphabet_position('H')
    expected = '8'
    assert result == expected
    result = alphabet_position('T')
    expected = '20'
    assert result == expected
    result = alphabet_position('Z')
    expected = '26'
    assert result == expected


def test_function_with_multiple_letters_no_space():
    result = alphabet_position('aHtZ')
    expected = "1 8 20 26"
    assert result == expected


def test_function_with_with_spaces():
    result = alphabet_position("The sunset sets at twelve o clock")
    expected = ("20 8 5 19 21 14 19 5 20 19 5 20 19 1 "
                "20 20 23 5 12 22 5 15 3 12 15 3 11")
    assert result == expected


def test_function_with_special_characters():
    result = alphabet_position("The#sunset()sets at twelve o' clock.")
    expected = ("20 8 5 19 21 14 19 5 20 19 5 20 19 1 "
                "20 20 23 5 12 22 5 15 3 12 15 3 11")
    assert result == expected
