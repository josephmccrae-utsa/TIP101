"""
Understand:
- Write function binary_search() with parameters nums and target.
- Return the index of target in nums.
Plan:
- Base Case: nums[middle] == target, return middle
- Recursive Case:
    - If nums[middle] < target, return middle+1 + binary_search(nums[middle+1:])
    - If nums[middle] > target, return binary_search(nums[:middle+1]) 
- Check case for if target is outside nums.
Implement:
"""

def binary_search(nums, target):
    left, right = 0, len(nums)-1
    middle = (left+right)//2

    if target < nums[left] or target > nums[right]:
        return None

    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        return middle+1 + binary_search(nums[middle+1:], target)
    else:
        return binary_search(nums[:middle+1], target)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 3)) 