def value(colors):
    code = ''
    for color in colors[:2]:
        code += str(color_code(color))
    return int(code)

def color_code(color):
    return colors().index(color)

def colors():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]