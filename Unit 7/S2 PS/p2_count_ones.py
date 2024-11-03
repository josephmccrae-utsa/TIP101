"""
Understand:
- Write function count_ones() with parameter lst.
- Return the total number of 1's in lst.
- Use Binary Search.
Plan:
- Create and intialize two pointers, left and right, representing the starting index and
last index of lst.
- Iterate until left > right:
    - Calculue the middle index between left and right.
    - If value of middle is 0,  initialize left to middle+1
    - Elif value of middle is 1, initialize right to middle-1.
    **Left will be initialized to the last 0 by the end of the loop.
- Return the difference of length of lst and left
Implement:
"""

def count_ones(lst):
    left = 0
    right = len(lst)-1

    while left <= right:
        middle = (right+left)//2 

        if lst[middle] == 0:
            left = middle + 1
        elif lst[middle] == 1:
            right = middle - 1
    

    return len(lst) - left

lst = [1, 1, 1, 1, 1, 1]
print(count_ones(lst))