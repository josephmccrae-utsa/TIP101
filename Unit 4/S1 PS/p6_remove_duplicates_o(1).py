"""
Understand:
- Write function remove_duplicates() that takes in sorted list of integers
nums as parameter and removes duplicates. 
- Do not use another array and only modify the original input list w/ O(1)
extra memory (constant space). 
- Return new length of lst.
Plan:
- Iterate through index of nums, incrementing every iteration via while loop.
- Compare the nums[index] to num[index+1], if they are the same, remove
nums[index+1] and decrement index.
- Return len(nums)
Implement:
"""
def remove_duplicates(nums):
    index = 0

    while(index < len(nums)-1):
        if(nums[index] == nums[index+1]):
            nums.remove(nums[index])
            index -= 1
        index += 1
    return len(nums)
    pass

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list