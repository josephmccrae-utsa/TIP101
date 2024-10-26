"""
Understand:
- Write function longest_uniform_substring() that has parameter string s,
and returns length of longest single repearted character in s.

Plan:
- Create variable length to track longest uniform string.
- Create index variable to iterate through s.
- Iterate through the index of s via a while loop.
- Create variable count to track the the current repeated value.
- If s[index] is the same as s[index+1], increment count by one. If count
is greater than length, length becomes count.
- Return length.

New Plan:
- Create empty dictionary.
- Iterate through s, adding each item into dictionary if it isn't there
and incremengting the value of the item if it is there.
- Iterate through the complete dictionary's values, intializaing the greatest
value to the variable length.
- return length.

Implement:
"""
def longest_uniform_substring(s):
    length = 0
    dict = {}
    for char in s:
        if char not in dict:
            dict[char] = 1  
        else:
            dict[char] += 1

    for value in dict.values():
        if value > length:
            length = value
    return length

    
    pass

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)