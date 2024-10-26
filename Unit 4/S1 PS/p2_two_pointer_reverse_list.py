"""
Understand:
- Write function reverse_list() that takes in list lst 
and return elements of the list in reverse order.
- Can not use list slicing (lst[::-1]).
- Use two-pointer approach.
    - Intialize two variables (pointers) to taack different indices of list.
    - Typically start and end of list.
    - Shift pointers inwards until they are equal or pass each other.
Plan:
- Initialize start pointer and end pointer of lst.
- While loop until pointers equal or end < start.
- Swap each item in list at start and end pointers every iteration.
- Increment start pointer and decrement end pointer every iteration.
- Return lst.
Implement:
"""
def reverse_list(lst):
    # start = 0
    # end = len(lst)-1
    start, end = 0, len(lst)-1

    while (start != end or start < end):
        # temp = lst[start]
        # lst[start] = lst[end]
        # lst[end] = temp
        lst[start], lst[end] = lst[end], lst[start]

        start += 1
        end -= 1
    return lst
    pass

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))