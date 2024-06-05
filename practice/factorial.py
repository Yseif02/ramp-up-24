def factorial_with_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_with_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_with_recursion(n - 1)

num = int(input("Enter a non-negative integer: "))

factorial_loop = factorial_with_loop(num)
print(f"Factorial using loops: {factorial_loop}")

factorial_recursion = factorial_with_recursion(num)
print(f"Factorial using recursion: {factorial_recursion}")