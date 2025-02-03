"""
Understand:
- Write function, is_valid(), that takes in String s as parameter.
- Return True if the input string is valid, False otherwise.
- An input String is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
Plan:
- Use recursion and eliminate each valid bracket in the input string if it
is valid. By the end of the recursion, return True when input string is
empty.
- Use a helper function to traverse through the string and determine if 
there is a valid bracket. Return the input string but with that valid
bracket eliminated.
Implement:
"""
def remove_bracket(s):
    for index in range(0, len(s)-1):
        if s[index:index+2] == '()' or s[index:index+2] == '[]' or s[index:index+2] == '{}':
            new_str = s[0:index] + s[index+2:]
            return new_str
    return s


def is_valid(s):
    print(s)
    if not s:
        return True
    
    new_str = remove_bracket(s)
    if s == new_str:
        return False
    
    return is_valid(new_str)
    

s = "()"
print(is_valid(s))

s = "(){}[]"
print(is_valid(s))

s = "(())"
print(is_valid(s))

s = "(}"
print(is_valid(s))

