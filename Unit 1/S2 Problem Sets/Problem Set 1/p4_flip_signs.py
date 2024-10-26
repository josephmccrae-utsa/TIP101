def flip_sign(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * -1)
    return new_lst


lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)