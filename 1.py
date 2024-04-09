def unique_elements(input_list):
    unique_set = set()
    repeated_set = set()
    
    for num in input_list:
        if num not in repeated_set:
            if num in unique_set:
                unique_set.remove(num)
                repeated_set.add(num)
            else:
                unique_set.add(num)
    
    return list(unique_set)


original_list = [1, 2, 3, 4, 5, 5, 6, 6]
unique_list = unique_elements(original_list)
print(unique_list)
