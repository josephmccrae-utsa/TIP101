"""
Understand:
- Write function find_largest_k() that takes in list of integers nums. 
- *nums doesn't contain any zeroes as a parameter.
- Function finds largest positive integer k such that -k also exists in
array and returns k.
- Nothing found, return -1.
Plan:
- Create variable largest_integer and intitialize it to -1.
- Iterate through nums via for loop.
- If num is greater than largest_integer and -num is in nums, 
largest_integer = num.
- Return largest_integer. 
Implement:
"""
def find_largest_k(nums):
    largest_integer = -1

    for num in nums:
        if (num > largest_integer and num*-1 in nums):
            largest_integer = num
    return largest_integer
    pass

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))