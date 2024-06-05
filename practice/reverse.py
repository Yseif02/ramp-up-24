def reverse_and_count_vowels(input_string):
    reversed_string = input_string[::-1]
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in reversed_string:
        if char.lower() in vowels:
            vowel_count += 1

    return reversed_string, vowel_count

input_string = input("Enter a string: ")
reversed_string, vowel_count = reverse_and_count_vowels(input_string)
print("Reversed string:", reversed_string)
print("Number of vowels:", vowel_count)