def max_difference(lst):
    max = lst[0]
    min = lst[0]

    for i in lst:
        if i < min:
            min = i
        if i > max:
            max = i

    return max - min

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)