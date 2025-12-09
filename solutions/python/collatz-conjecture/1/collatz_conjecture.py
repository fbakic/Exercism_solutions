def steps(number):
    if number <= 0 or isinstance(number, int) == False:
        raise ValueError("Only positive integers are allowed")
    else:
        steps = [number]
        while steps[-1] != 1:
            if steps[-1] % 2 == 0:
                steps.append(steps[-1]/2)
            else:
                steps.append(steps[-1]*3 + 1)
    return len(steps)-1
        