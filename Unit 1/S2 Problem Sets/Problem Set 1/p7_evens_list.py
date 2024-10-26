def get_evens(lst):
    new_lst = []
    for i in lst:
        if (i % 2 == 0):
            new_lst.append(i)
    return new_lst

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)