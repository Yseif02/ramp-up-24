def number_split(num):
    half = num // 2
    if num % 2 == 0:
        return [half, half]
    else:
        return [half, half + 1]
    