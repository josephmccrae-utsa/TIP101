"""
Understand:
- Writing function is_prime() that takes in paramter positive integer n.
- Return True if n is prime, False otherwise.
- Prime divisible by one and itself.
Plan:
- Return False if n < 1.
- Create variable x, initalize to 2.
- While loop until x = n-1
- If n % x == 0, return False.
- Return True
Implement:
"""
def is_prime(n):
    x = 2

    while (x < n-1):
        if n % x == 0:
            return False
        x += 1

    return True


print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
print(is_prime(7))
print(is_prime(24))