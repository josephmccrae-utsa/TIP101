"""
Understand:
- Write function is_nested() with parameter paren_s (string of parentheses).
- Function should return True if the paren_s is a nesting of zero or more pairs of
parentheses.
- Return False otherwise.
Plan:
- Base Case: If paren_s == "", return True.
- Sub-Problem: N/A
- Recursive Case: is_nested(paren_s)

- Check paen_s until "()", and pop it out, then call the recursive case.
Implement:
"""
def is_nested(paren_s):
    if len(paren_s) % 2 == 1:
        return False
    
    if paren_s == "":
        return True

    # paren_s = "(((())))"

    if paren_s[0] == "(" and paren_s[-1] == ")":
        return is_nested(paren_s[1:-1])
    
    else:
        return False
    
paren_s = "(())"

print(is_nested(paren_s))

""