"""
Understand:
- Write function is_pangram() with my_str as parameter.
- Return True if string is a pangram (sentence containing every letter 
of alphabet).

Plan:
- Create an empty dictionary, dict, to count occurences of each character in my_str.
- Iterate through my_str and use lower() method to account for capitalization.
- Add each character to dict if not found in dict.
- Return True if number of keys in dict equals 26, the number of letters in alphabet.
- False otherwise. 
Implement:
"""

def is_pangram(my_str):
    dict = {}

    for char in my_str.lower():
        if char != ' ':
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        """if char == ' ':
            dict.pop(' ')"""

    if len(dict.keys()) == 26:
        return True
    return False

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))