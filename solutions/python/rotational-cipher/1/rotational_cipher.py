from string import ascii_lowercase
def rotate(text, key):
    final = ''
    for element in text:
        if not element.isalpha():
            final += str(element)
            
        elif element.isupper():
            position = (ascii_lowercase.index(element.lower()) + key) % 26
            final += str(ascii_lowercase[position].upper())

        else:
            position = (ascii_lowercase.index(element) + key) % 26
            final += str(ascii_lowercase[position])

    return final