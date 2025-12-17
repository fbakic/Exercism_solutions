actions = ["Reverse the order of the operations in the secret handshake",
           "jump",
           "close your eyes",
           "double blink",
           "wink"]

def commands(binary_str):
    result = [actions[i] for i in range(4,0,-1) if int(binary_str[i])]
    if int(binary_str[0]):
        result.reverse()
    return result