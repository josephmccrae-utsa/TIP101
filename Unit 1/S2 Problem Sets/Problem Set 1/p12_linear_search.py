def linear_search(lst, target):
    for i in range(len(lst)):
        if(lst[i] == target):
            return i
    return -1


lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)