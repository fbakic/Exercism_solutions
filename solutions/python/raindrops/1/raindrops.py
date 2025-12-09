def convert(number):

    div_3 = 'Pling' if number % 3 == 0 else ''
    div_5 = 'Plang' if number % 5 == 0 else ''
    div_7 = 'Plong' if number % 7 == 0 else ''
    div_else = (str(number) if number % 3 != 0 and number % 5 != 0 and number % 7 != 0  else '')

    return div_3 + div_5 + div_7 + div_else