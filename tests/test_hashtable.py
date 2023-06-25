import pytest

from hashtable.hashtable import Hashtable

def test_hashtable_testone():
    hash_table = Hashtable()
    expected = 5
    actual = len(hash_table.table)
    assert expected == actual

def test_hashtable_add_new_item():
    hash_table = Hashtable()
    hash_table.set("Abdullah", 30)
    expected = ["Abdullah"]
    actual = hash_table.keys()
    assert expected == actual
    
    
def test_hashtable_has(test_HT):
    assert test_HT.has("Abdullah") == True
    
def test_hashtable_get(test_HT):
    assert test_HT.get("Abdullah") ==  30
    
def test_hashtable_keys(test_HT):
    assert test_HT.keys() == ["Nawras", "Abdullah", "Amjad","Abdullah shaghnobah"]

@pytest.fixture
def test_HT():
    hash_table = Hashtable()
    hash_table.set("Abdullah", 30)
    hash_table.set("Amjad", 26)
    hash_table.set("Abdullah shaghnobah", 28)
    hash_table.set("Nawras", 24)
    return hash_table