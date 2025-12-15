def reverse(text):
    original_text = list(text)
    reversed_text = ''
    while len(original_text) > 0:
        reversed_text += original_text[-1]
        original_text.pop(-1)
    return reversed_text