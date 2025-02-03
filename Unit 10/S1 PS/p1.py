"""
Understand:
- Write function is_vald() with parameter s (string).
- Return True if input string valid, False otherwise.
- Input string is valid:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
Plan:
- Recursively eliminate valid brackets within the input string until it becomes 
empty. Return True if that case, False if we did not eliminate a valid bracket 
(means the input string is invalid).

- Base Case: If not s, return True.
- If s = new_str:
    - Return False
- Recursive Case: is_valid(new_str), new_str is the modified string.

- Create a helper function, valid_bracket() with parameter s. 
    - Iteratively compare consecutive indeces to valid pairs of brackets
        - Once found a valid bracket:
            - Return new_str (modified string with the eliminated valid bracket)
    - Not found valid bracket? Return s
Implement:
"""
def is_valid(s):
    if not s:
        return True
    
    def valid_bracket(s):
        for index in range(0, len(s)-1):
            if s[index:index+2] == "()" or s[index:index+2] == "[]" or s[index:index+2] == "{}":
                new_str = s[0:index] + s[index+2:]
                return new_str
        return s
    
    new_str = valid_bracket(s)
    if s == new_str:
        return False

    return is_valid(new_str)

s = "()"
print(is_valid(s))

s = "()[]{}"
print(is_valid(s))

s = "(())"
print(is_valid(s))

s = "(]"
print(is_valid(s))