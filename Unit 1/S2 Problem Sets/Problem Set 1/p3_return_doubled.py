def doubled(lst):
    new_lst = []
    
    for i in lst:
        new_lst.append(i * 2)
    
    return new_lst




lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)