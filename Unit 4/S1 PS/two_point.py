"""
Understand:
- Write function reverse_list() that takes in parameter list lst.
- Return elements of list in reversed order.
- Not allowed to use list slicing (lst[::-1])
Plan:
- Create start pointer, intialized at 0.
- Create end pointer, initalized at len(lst)-1
- While loop through lst, until start = end or start > end (end < start).
- Swap items in lst 
- Increment the start pointer, decrement the end pointer.
- Return Swapped lst.
Implement:
"""
def reverse_list(lst):
    start = 0
    end = len(lst)-1

    while(start != end or start < end):
        lst[start], lst[end] = lst[end], lst[start]

        start += 1
        end -= 1
    return lst
    pass

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))