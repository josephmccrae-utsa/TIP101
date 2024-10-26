"""
Understand:
- Write function reverse_only_letters() that tasks string s as parameter.
- THe function reterns a new string of the reversed order of s.
- Non-letter characters should remain in orignal positions.
Plan:
- Create new string str and initialize to an empty string.
- Create a new string reversed to hold reversed letters.
- Create a variable to hold index of s (later).
- Iterate through the index, i, of s to reverse the letters
- Check if the character at i is alphabetical. If it is, concatenate the 
character at the end of the string (- indeces).

- Iterate again through s in terms of each character, char.
- Check if the char is alphabetical. If so, concatenate str with the
reversed string at index and increase value of index by one. If not,
concatenate str with the non-alphabetical value.
- Return str.
Implement:
"""

def reverse_only_letters(s):
    str = ""
    reversed = ""
    index = 0
    
    # String of reversed letters.
    for i in range(0, len(s)):
        if s[-i-1].isalpha():
            reversed += s[-i-1]
    print(reversed)

    for char in s:
        if char.isalpha():
            str += reversed[index]
            index += 1
        else:
            str += char
    
    return str
    pass

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)