def print_negatives(lst):
    num = len(lst)
    for i in lst:
        if i < 0:
            print(i)
            num -= 1
    if num == len(lst):
        print(None)
        

print_negatives([3,-2,2,1,-5])

print_negatives([1,2,3,4,5])