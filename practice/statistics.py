def calculate_statistics(numbers):
    if not numbers:
        print("The list is empty.")
        return

    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)

    print("Sum:", total)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", average)

numbers = [1, 2, 3, 4, 5]
calculate_statistics(numbers)