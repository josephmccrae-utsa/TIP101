def is_subsequence(lst, sequence):
    counter = 0
    for item in lst:
        for element in sequence:
            if element == item:
                counter += 1
    if counter == len(sequence):
        return True
    return False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

