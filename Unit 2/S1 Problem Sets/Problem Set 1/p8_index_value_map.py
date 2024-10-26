def index_to_value_map(lst):
    dictionary = {}
    for index in range(len(lst)):
        dictionary[index] = lst[index]

    return dictionary

lst = ["apple", "banana", "cherry"]

print(index_to_value_map(lst))