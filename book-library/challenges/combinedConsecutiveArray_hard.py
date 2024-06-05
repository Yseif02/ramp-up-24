def consecutive_combo(lst1, lst2):
    combinedUnsorted = lst1 + lst2
    print(combinedUnsorted)
    combined = sorted(lst1 + lst2)
    print(combined)
    for i in range(len(combined) - 1):
        if combined[i] + 1 != combined[i + 1]:
            return False
    return True

print(consecutive_combo([7, 4, 5, 1], [2, 3, 6])) # True
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])) # False
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])) # False
print(consecutive_combo([44, 46], [45])) # True
print(consecutive_combo([4, 3, 1], [2, 5])) # True
print(consecutive_combo([4, 3, 1], [2, 5, 6])) # True