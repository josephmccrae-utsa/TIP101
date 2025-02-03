"""
Understand:
- Write function, remove_element(), with parameters nums (integer list) and 
val (integer).
- Remove all occurences of val in nums in-place (O(1) space complexity)
- Return the number of elements in nums that are not equal to val (k).
- We also want to reaarange the list where the unequal values appear within the
first k elements in nums.
Plan:
- Initalize variable k, the number of elements in nums unequal to val.
- Traverse through the indeces of nums via for loop.
    - If the value at the index of nums is equal to val,
        - Remove the valud at the index of nums
    - Else
        - Increment k.
- Return k
Implement:
"""
def remove_element(nums, val):
    k = 0

    index = 0
    while index < len(nums):
        if nums[index] == "-":
            break
        if nums[index] == val:
            nums.remove(nums[index])
            index -=1
            nums.append("-")
        else:
            k+=1
        index += 1

    
    return k

nums = [3,2,2,3] 
val = 3
print(remove_element(nums, val))

nums = [0,1,2,2,3,0,4,2] 
val = 2
print(remove_element(nums, val))