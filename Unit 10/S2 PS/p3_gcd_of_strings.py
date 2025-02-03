"""
Understand:
- Write function gcd_of_strings(), with parameters str1 and str2.
- Return the largest string x such that x divides both str1 and str2.
Plan:
- 
Implement:
"""
def helper(str1, div):
    if str1 == "":
        return 0
    else:
        return 1 + 