def is_armstrong_number(number):
    amstg_nums = list(str(number))
    exponent = len(amstg_nums)
    sum = 0
    for num in amstg_nums:
        sum += int(num) ** exponent
    return sum == number