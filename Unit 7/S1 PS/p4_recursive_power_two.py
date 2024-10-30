"""
Understand:
- Write function is_power_of_two() that takes parameter positive integer nm.
- Return True if n is a power of two, otherwise false.
Plan:
- Base Case: If n < 1, return False
- Sub problem: is_power_of_two(n/2)
- Recursive Case: is_power_of_two(n/2)
Implement:
"""


def is_power_of_two(n):
    if n == 2: 
        return True
    elif n % 2 == 1:
        return False
    
    return is_power_of_two(n/2)

print(is_power_of_two(10))