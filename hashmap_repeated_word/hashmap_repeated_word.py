def repeated_word(str):
    hash_map = {}
    for word in str.split():
        if word.lower() in hash_map:
            return word
        else:
            hash_map[word.lower()] = True