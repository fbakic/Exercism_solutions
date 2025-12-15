def is_valid(isbn):
    sum=0
    d_list = []
    
    for num in isbn:
        if num == 'X': d_list.append(10)
        elif num == '-': continue
        elif not(num.isnumeric()): return False
        else: d_list.append(int(num))

    if len(d_list) != 10:
        return False
    elif 'X' in isbn and d_list[-1] != 10:
        return False
    else:
        for i in range(10):
            sum += d_list[i]*(10-i)
        return sum % 11 == 0

    