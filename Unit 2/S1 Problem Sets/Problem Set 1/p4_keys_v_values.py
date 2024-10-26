def keys_v_values(dictionary):
    sumKeys = 0
    sumValues = 0

    for key in dictionary.keys():
        sumKeys += key
    for value in dictionary.values():
        sumValues += value

    if sumKeys > sumValues:
        return "keys"
    elif sumKeys < sumValues:
        return "values"
    elif sumKeys == sumValues:
        return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

dictionary3 = {1:1, 2:2, 3:3}
greater_sum = keys_v_values(dictionary3)
print(greater_sum)