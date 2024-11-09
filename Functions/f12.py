# Write a function remove_duplicates(lst) that removes duplicate  elements from a list. 

def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:  
            unique.append(item)
    return unique
# we can also simply do: ```return list(set(lst))``` , where set removes duplicates and is again converted to list after removal
