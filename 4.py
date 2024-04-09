def sort_by_length(strings):
    sorted_by_length_asc = sorted(strings, key=len)
    sorted_by_length_desc = sorted(strings, key=len, reverse=True)
    return sorted_by_length_asc, sorted_by_length_desc


strings = ["apple", "banana", "orange", "kiwi", "grape"]
asc_sorted, desc_sorted = sort_by_length(strings)

print("Sorted by length in ascending order:", asc_sorted)
print("Sorted by length in descending order:", desc_sorted)
