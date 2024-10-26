"""
Understand:
- Write function is_prime() that takes positive integer n and returns True
if a prime number and false otherwise. 
- A prime number greater than 1 has no positive divisors other than 1 and itself.
Plan:
- Create a variable, x, that will increment to positive integer n and 
initalize at 2.
- While loop from x to n-1 and increment x every iteration.
- If n is divisible by x (use modulo operator), then return False.
- Return True otherwise.
- ALso, if n equals 1, return True.
Implement:
"""
def is_prime(n):
    x = 2

    if(n == 1):
        return True
    
    while(x < n-1):
        if(n % x == 0):
            return False
        x += 1
    return True
    pass

print(is_prime(3))
print(is_prime(12))
print(is_prime(9))