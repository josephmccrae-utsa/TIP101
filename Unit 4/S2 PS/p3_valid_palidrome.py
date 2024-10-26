"""
Understand:
- Write function valid_palidrome() that takes in string s as parameter.
- Return true if s can be a palidrome after deleting at most one character
from it and False otherwise.
Implement:
- Make a helper function that returns a deleted character from string s at
index i.
    - Create an empty string, new_str
    - Iterate through index of s via for loop.
    - If index != i, add char to new_str.
    - Return new_str. 
- First, if s == s[::-1], return True (Case for if s is already palindrome)
- Iterate through index of s via for loop. 
- Create new string variable str, intiialized to return of helper string at
parameter s and index.
- Check if str == str[::-1], return True if found.
- Return False.
Plan:
"""
def deleted_char(s, i):
    new_str = ""

    for index in range(len(s)):
        if(index != i):
            new_str += s[index]
    return new_str
    pass

def valid_palindrome(s):
    if s == s[::-1]:
        return True
    
    for index in range(len(s)):
        str = deleted_char(s, index)
        if str == str[::-1]:
            return True
    return False
    pass

s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))