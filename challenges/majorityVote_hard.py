def majority_vote(lst):
    if len(lst) == 0:
        return None
    
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    
    max_item = None
    max_count = 0
    for item, count in counts.items():
        if count > max_count:
            max_item = item
            max_count = count
    
    if max_count > len(lst) / 2:
        return max_item
    
    return None

print(majority_vote(["A", "A", "A", "B", "C", "A"])) # A
print(majority_vote(["A", "A", "A", "B", "B", "A"])) # A
print(majority_vote(["A", "A", "A", "A", "B", "B"])) # A
print(majority_vote(["A", "B", "B", "A", "C", "C"])) # None
print(majority_vote(["B", "B", "A", "B", "B", "C"])) # B
