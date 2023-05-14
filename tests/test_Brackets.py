import pytest
from Stack_and_queues_brackets.Stack_and_queues_brackets import validate_brackets

def test_1 ():
    assert validate_brackets("[[{}]]") == True


def test_2 ():
    assert validate_brackets("[[{}]") == False


def test_3 ():
    assert validate_brackets("aa[[{AMJAD}]aa]") == True

def test_4 ():
    assert validate_brackets("[[{())()()}]]())())(){{{()()}}}") == False