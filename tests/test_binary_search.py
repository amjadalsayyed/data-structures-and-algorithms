import pytest
from array_binary_search.array_binary_search import binary_search

def test1():
    array=[1,2,3,4,5,6]
    target=3
    assert binary_search(array,target) == 2
def test2():
    array=[4, 8, 15, 16, 23, 42]
    target=15
    assert binary_search(array,target) == 2
def test3():
    array=[-131, -82, 0, 27, 42, 68, 179]
    target=42
    assert binary_search(array,target) == 4
def test4():
    array=[11, 22, 33, 44, 55, 66, 77]
    target=90
    assert binary_search(array,target) == -1