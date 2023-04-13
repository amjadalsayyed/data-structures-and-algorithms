import pytest

from linked_lists.linked_list import LinkedList

def test_1():
    ll = LinkedList()
    assert str(ll) == "Empty LinkeList"

def test_2(AA):
    assert str(AA) == "C -> B -> A ->  Null"

def test_3():
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    assert str(ll) == "B -> A ->  Null"

def test_4(AA):
    assert AA.includes('A') == True

def test_5(AA):
    assert AA.includes('D') == False

def test_6(AA):
    assert AA.head.value == "C"    

    
@pytest.fixture
def AA():
    AA = LinkedList()
    AA.insert('A')
    AA.insert('B')
    AA.insert('C')
    return AA