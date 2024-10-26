"""
Find majority element in list. Majority meaning that it
appears more than n/2 times where n is the size of list.
No majority? Return None.
"""

def find_majority_element(elements):
    dict = {}
    for element in elements:
        if element not in dict:
            dict[element] = 1 
        elif element in dict:
            dict[element] += 1

    # max method returns key with highest value using the values corresponding
    # to the keys in the dictionary as the measurement
    return max(dict, key=dict.get) 

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))

