import pytest
from mock_inteview.mock_interview import row_sums

def test_mock1():
    array = [ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]
    assert row_sums(array) == [6,15,18]
def test_mock2():
    array = [ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ]
    assert row_sums(array) == [6, 5, 20]