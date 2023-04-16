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

def test_7(AA):
    expected = "C -> B -> A -> D ->  Null" 
    AA.append("D")
    actual = str(AA)       
    assert expected == actual 

def test_8(AA):
    expected = "C -> B -> A -> D -> E ->  Null" 
    AA.append("D")
    AA.append("E")
    actual = str(AA)       
    assert expected == actual 

def test_9(AA):
    expected = "C -> B -> g -> A ->  Null" 
    AA.insert_before('A','g')
    actual = str(AA)       
    assert expected == actual 

def test_10(AA):
    expected = "g -> C -> B -> A ->  Null" 
    AA.insert_before('C','g')
    actual = str(AA)       
    assert expected == actual 

def test_11(AA):
    expected = "C -> B -> f -> A ->  Null" 
    AA.insert_after('B','f')
    actual = str(AA)       
    assert expected == actual

def test_12(AA):
    expected = "C -> B -> A -> f ->  Null" 
    AA.insert_after('A','f')
    actual = str(AA)       
    assert expected == actual



    
@pytest.fixture
def AA():
    AA = LinkedList()
    AA.insert('A')
    AA.insert('B')
    AA.insert('C')
    return AA