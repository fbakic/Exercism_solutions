from string import ascii_lowercase
alphabet = set(ascii_lowercase)

def is_pangram(sentence):
    return alphabet <= set(sentence.lower())

