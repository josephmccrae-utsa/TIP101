def above_threshold(lst, threshold):
    out_lst = []
    for i in lst:
        if i > threshold:
            out_lst.append(i)
    return out_lst

lst = [8,2,13,11,4,10,14]
new_lst = above_threshold(lst, 10)
print(new_lst)