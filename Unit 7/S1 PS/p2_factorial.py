"""
Understand:
- Write function factorial() with parameter integer n.
- Return the factorial of n.
Plan:
- Sub-problem: n-1
- Base case: 1 when n = 0
- Recursive Case: factorial(n) = n * factorial(n-1)
Implement:
"""

def factorial(n):
    if n < 0:
        return None
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

