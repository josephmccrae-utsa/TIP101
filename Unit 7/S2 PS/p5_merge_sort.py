# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
    result = [] # List to store the merged result
    i = j = 0 # Pointers to iterate over left and right input arrays
    
    # Compare elements from left and right halves of the list and add them to the
    # result list in the correct order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements from the left half to the result list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right half to the result list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

"""
Understand:
- Write function merge_sort() with parameter lst (unsorted list).
- Return lst (sorted List).
- Use Merge Sort method with the helper function merge().
Plan:
- Divide lst into two halves, repeatedly, until each sublist contains a 
single element, then recursively sort via merge().
- Base Case: If len(lst) == 1, then return lst
- Recursive Case: merge_sort(halved_lst) 
Implement:
"""
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    new_lst = lst
    middle = len(new_lst)//2

    lst1 = new_lst[:middle]
    lst2 = new_lst[middle:]

    lst1 = merge_sort(lst1)
    lst2 = merge_sort(lst2)
    
    return merge(lst1, lst2)


lst = [5, 4, 3, 2, 1]
print(merge_sort(lst))