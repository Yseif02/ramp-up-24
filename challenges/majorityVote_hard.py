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

