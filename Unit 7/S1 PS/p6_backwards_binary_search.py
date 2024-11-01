"""
Undrestand:
- Write function find_last() with parameters lst and target.
- Returns the index of the last occurence of target.
Plan:
- Use the previous binary search to start.
- Create variable, found, initialized at -1 to represent the index of 
target if found in lst.
- When the value of middle equals target, initalize found with middle and
initalize left with middle + 1 to still check the rest of lst to see if
there is another value equal to target (until the last one).
- ALso, loop until lest <= right in case right to account for consecutive 
values at the end of lst.
Implement:
"""
def find_last(lst, target):
    left = 0
    right = len(lst)-1
    found = -1

    while left <= right:
        middle = int((right+left)/2) 

        if lst[middle] == target:
            found = middle
            left = middle + 1
        elif lst[middle] < target:
            left = middle + 1
        else:
            right = middle + 1
    
    return found

lst = [1, 3, 3, 5, 7, 9, 11, 11, 13, 15, 15]
print(find_last(lst, 15))
    