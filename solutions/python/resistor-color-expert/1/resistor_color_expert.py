def resistor_label(colors):
    suffixes = [' ohms ±', ' kiloohms ±', ' megaohms ±', ' gigaohms ±']
    
    if len(colors) == 1:
        return '0 ohms'  
    
    if len(colors) == 4:
        code = (10*value(colors[0]) + value(colors[1])) * 10**value(colors[2])
        tolerance= resistors(colors[3])

    else:
        code = (100*value(colors[0]) + 10*value(colors[1]) + value(colors[2])) * 10**value(colors[3])
        tolerance = resistors(colors[4])

    for i in range(4):
        exponent = 1000**(3-i)
        if code // exponent > 0:   
            if (code/exponent).is_integer():
                return str(int(code/exponent)) + suffixes[3-i] + tolerance
            else:
                return str(code/exponent) + suffixes[3-i] + tolerance
                
def value(colors):
    codes = {"black":0, "brown":1, "red":2, "orange":3,
             "yellow":4, "green":5, "blue":6, "violet":7,
             "grey":8, "white":9}
    
    return codes[colors] 

def resistors(colors):
    codes = {"grey":"0.05%", "violet":"0.1%", "blue":"0.25%", "green":"0.5%",
             "brown":"1%", "red":"2%", "gold":"5%", "silver":"10%"}
    return codes[colors]