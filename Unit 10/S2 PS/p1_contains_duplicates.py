"""
Understand:
- Write function, contains_duplicated(),  with parameter nums (array).
- Return True if any value appears twice in the array, False otherwise.
Plan:
- Initialize empty dictionary dict.
- Traverse through nums, initializing each value into dict if not there
    - If value is already in dict, return True.
- Return False.
Implement:
"""
def contains_duplicate(nums):
    dict = {}

    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            return True
        
    return False


nums = [1,2,3,1]
print(contains_duplicate(nums))

nums = [1,2,3,4]
print(contains_duplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums))
