"""
Understand:
- Write a function to find the first non-repeating character in given string
and return its index. If not found, return -1.

Plan:
- Create empty dictionary.
- Initialize every character of my_str to dictionary. Add 1 to value
if already in dictionary.
- Loop through dictionary  and find the first key of value 1. Return it's 
index in my_str.
- Iterate through my_str to find the index of that key.
Implement:
"""
def first_unique_char(my_str):
    dict = {}
    
    for char in my_str:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    first_unique = ""
    for key, value in dict.items():
        if value == 1:
            first_unique = key
            break
    
    for index in range(0, len(my_str)):
        if my_str[index] == first_unique:
            return index
    
    return -1
    pass

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))