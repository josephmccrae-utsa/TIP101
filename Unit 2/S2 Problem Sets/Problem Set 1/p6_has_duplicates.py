"""
Understand:
- Find the duplicate values in a given list, nums, and return True if found.
- Iteration up to given parameter k in nums.
- False if no duplicate is found.

Plan:
- Determine if k is greater than range of nums.
- Iterate through nums and compare each num to each other (may require another loop).
- Return True whenever anything is equal. False otherwise.

New Plan:
- Create dictionary recording num in nums up to range 0 to k.
- If any key,value pair has a value greater than 1, return True. False otherwise.

New New Plan:
- Create dictionary record num in nums up to range 0 to k.
- If any new value to be added into dictionary is already in there. Return True
- False otherwise
*** Likely better with sets but dictionaries can work too.
Implement:
"""

def hasDuplicates(nums, k):
    dict = {}
    if k > len(nums):
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
    else:
        for i in range(0, k+1):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                return True

    return False

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 4)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)