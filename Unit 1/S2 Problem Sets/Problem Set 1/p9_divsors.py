def find_divisors(n):
    divisors = []

    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

lst = find_divisors(6)
print(lst)