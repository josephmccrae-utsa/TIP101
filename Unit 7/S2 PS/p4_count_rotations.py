"""
Understand:
- Write function count_rotations() with parameter nums (list of integers).
- Return number of times nums has rotated.
Plan:
- Goal is to determine the index where nums breaks sort (when value at index is 
greater than value at index+1).
- Iterate through indeces of nums via for loop.
    - If nums[index] > nums[index+1], return index+1.
- Return 0.
Implement:
"""
def count_rotations(nums):

    for index in range(0, len(nums)-1):
        if nums[index] > nums[index+1]:
            return index+1
    return 0
    
nums = [8, 9, 10, 2, 5, 6]
print(count_rotations(nums))