"""
Understand:
- Write function sum_list() that takes parameter lst.
- Return the sum of all the values in lst.
- Don't use sum() function.
Plan:
- Sub-problem: lst.pop(0)
- Base Case: len(lst)== 1 return lst[0]
- Recursive Case: lst[len(lst-1)] + sum_list(lst.pop())
Implemment:
"""

def sum_list(lst):
    if len(lst) == 0:
        return 0

    temp = lst.pop()
    return temp + sum_list(lst)

lst = [1, 2, 3, 4, 5]
print(sum_list(lst))
