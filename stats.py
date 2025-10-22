def word_count(stored): # <--- Problem 2: 'total' should not be a parameter here.
    words = stored.split()
    total = len(words)   # <--- Problem 3: This function still needs a 'return' statement!
    return total
def text_filter(stored):
    empty = {}
    for ch in stored.lower():
            empty[ch] = empty.get(ch, 0) + 1
    return empty
def sort_on(item):
    return item["num"]

def dict_to_sorted_list(empty):
    result = []
    for ch, count in empty.items():
        if ch.isalpha():
            result.append({"char":ch,"num":count})
    result.sort(reverse=True, key=sort_on)
    return result