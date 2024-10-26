"""
Understand:
- Write function contains_nearby_duplicate() that takes in list lst and 
positive number k as parameters.
- Returns True if list contains any duplicate elmenets within range k.
False otherwise.
If k is greater than list's size, solution checks for complete list.
Plan:
- Create helper function, contains_dupe() that takes in parameter list lst
and returns True of there is a duplicate element in lst.
    - Create empty dictionary, dict.
    - Iterate through each element of lst.
    - If element is not in dict, add it to dict.
    - IF element is already in dict, return True
    - Return False.
- If k > len(lst), k = len(lst).
- Iterate through index of lst via for loop.
- Check contains_dupe(sub_lst) for every sub_lst = lst[index:index+k]
- If True, return True. 
- Return False.
Implement:
"""
def contains_dupe(lst):
    dict = {}

    for element in lst:
        if element not in dict:
            dict[element] = 1
        elif element in dict:
            return True
    return False
    pass

def contains_nearby_duplicate(lst, k):
    if k > len(lst):
        k = len(lst)
    for index in range(0, len(lst)):
        if contains_dupe(lst[index:index+k+1]):
            return True
    return False
    pass

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))