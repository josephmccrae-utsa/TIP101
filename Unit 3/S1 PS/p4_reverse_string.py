"""
Understand:
- Return the reversed string of my_str
Plan:
- Create new_str to contain the reversed string values.
- Iterate through the range of the length of my_str string for every index.
- Add characters from the ends of my_str to new_str.
- Return new_str.
Implement:
"""

def reverse_string(my_str):
    new_str = ""

    for index in range(1, len(my_str) + 1):
        new_str += my_str[-index] 
    return new_str
    pass

my_str = "live"
print(reverse_string(my_str))