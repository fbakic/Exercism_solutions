def is_isogram(string):
    iso = []
    for char in string:
        if char.lower() not in iso or char in [" ","","-"]:
            iso.append(char.lower())
    return len(iso) == len(list(string))