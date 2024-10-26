"""
Understand:
- Write function remove_duplicates() that takes a sorted list of integers
nums and removes all duplicates in teh list. 
- Return modified list.

Plan:
- Iterate through nums and if the next integer in the list is the same as 
the current one, remove it.
- Return modified list.

New Plan:
- Iterate through nums through a while loop.
- Once we find a duplicate in the nums, remove it until there are no duplicates
of that num left via a while loop.
- Return modified list. 

Implement:
"""
def remove_duplicates(nums):
    index = 0

    while index < len(nums)-1:
        if nums[index] == nums[index+1]:
            nums.remove(nums[index+1])
            index -= 1
        
        index += 1

    
    return nums
    pass

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))