def label(colors):
    code = int(str(value(colors[0])) + str(value(colors[1])) + value(colors[2])*'0')
    suffixes = [' ohms', ' kiloohms', ' megaohms', ' gigaohms']
    
    if code == 0:
        return '0 ohms'
    
    for i in range(4):
        exponent = 1000**(3-i)
        if code // exponent > 0:
            return str(int(code/exponent)) + suffixes[3-i]

def value(colors):
    codes = {"black":0, "brown":1, "red":2, "orange":3,
             "yellow":4, "green":5, "blue":6, "violet":7,
             "grey":8, "white":9}
    
    return codes[colors] 