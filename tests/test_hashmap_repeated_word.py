import pytest


from hashmap_repeated_word.hashmap_repeated_word import repeated_word 

def test_hashmap_repeated_word_testone():
    text = "Once upon a time, there was a brave princess who..."
    hash_table = repeated_word(text)
    expected = 'a'
    actual = hash_table
    assert expected == actual


def test_hashmap_repeated_word_two_testone():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light. "
    hash_table = repeated_word(text)
    expected = 'it'
    actual = hash_table
    assert expected == actual    

def test_hashmap_repeated_word_three_testone():
    text = "It was a queer, sultry summer , the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    hash_table = repeated_word(text)
    expected = 'summer'
    actual = hash_table
    assert expected == actual