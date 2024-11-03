"""
Understand:
- Write function search_circular_list() with parameters nums and target.
- Function should return the index of target.
Plan:
- Use binary search to determine the index of target.
- Issue is the list isn't sorted correctly, so determine if the list is 
sorted before initalized pointers.
Implement:
"""
def search_circular_list(nums, target):
    left, right = 0, len(nums)-1
    
    while left <= right:
        middle = (right+left)//2

        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]: # If left half is sorted
            if nums[left] <= target < nums[middle]: # If target in left half
                right = middle - 1
            else:
                left = middle + 1
        else:
            if nums[middle] < target <= nums[right]: # If target in right half
                left = middle + 1 
            else:
                right = middle - 1
    
    return -1


nums = [8, 9, 10, 2, 5, 6]
print(search_circular_list(nums, 7))