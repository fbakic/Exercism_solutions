def response(hey_bob):
    trimmed = hey_bob.strip()

    #Silence
    if trimmed == "":
        return "Fine. Be that way!"
    
    letters = [c for c in trimmed if c.isalpha()]
    yelling = letters and all(c.isupper() for c in letters)
    question = trimmed.endswith("?")

    #Prediction
    if yelling and question:
        return "Calm down, I know what I'm doing!"
    elif yelling:
        return "Whoa, chill out!"
    elif question:
        return "Sure."
    else:
        return "Whatever."