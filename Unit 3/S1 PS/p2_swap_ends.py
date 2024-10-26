"""
Understand:
- Write function swap_ends() that accepts string parameter and returns
new string where first and last characters from original string are swapped.

Plan:
- Create a list, charList, to separate chracters of orignial string.
- Also create and initialize temp char as the first char in charList
- Set the first character in charList to the last value.
- Set the last character in charList to temp char (original first value)
- Use join() method to create a newString of the modified character values.

New Plan: 
- Use String indexxing and slicing to create a new String with the swapped
values.
- Create new_str.
- Initialize with the last value, then the middle, finally the first of my_str.

Implement:
"""

def swap_ends(my_str):
    """
    char_list = list(my_str)
    temp = char_list[0]

    char_list[0] = char_list[len(char_list)-1]
    char_list[len(char_list)-1] = temp
    
    new_str = "".join(char_list)
    return new_str
    """
    new_str = my_str[-1] + my_str[1:-1] + my_str[0]
    return new_str
    pass

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)