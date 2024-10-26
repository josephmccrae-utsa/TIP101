"""
Understand:
- Write function sort_list_by_parity() that takes in integer list nums
and move all even integers to beiginning of the list followed by odd 
integers. Order is irrelevant.
Plan:
- Create start pointer, initialized to 0.
- Create end pointer, initialized to len(nums)-1
- Iterate through nums via while loop, until start = end or start > end
- If nums[start] is odd and nums[end] is even, swap and increment/decrement
- If nums[start] is even, increment start.
- Return nums.
Implement:
"""
def sort_array_by_parity(nums):
    start = 0
    end = len(nums)-1

    while(start != end and start < end):
        if nums[start] % 2 == 1 and nums[end] % 2 == 0:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        elif nums[start] % 2 == 0:
            start += 1
        else:
            end -= 1
    return nums
    pass

nums = [3,1,2,4,8,7,6,5,5,4,3,2]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))