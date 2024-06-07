
def consecutive_combo(lst1, lst2):
    # combinedUnsorted = lst1 + lst2
    # print(combinedUnsorted)
    combined = sorted(lst1 + lst2)
    # print(combined)
    for i in range(len(combined) - 1):
        if combined[i] + 1 != combined[i + 1]:
            return False
    return True
