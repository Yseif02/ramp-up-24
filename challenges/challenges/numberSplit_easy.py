def number_split(num):
    half = num // 2
    if num % 2 == 0:
        return [half, half]
    else:
        return [half, half + 1]
    
print(number_split(4)) # [2, 2]
print(number_split(10)) # [5, 5]
print(number_split(11)) # [5, 6]
print(number_split(-9)) # [-5, -4]