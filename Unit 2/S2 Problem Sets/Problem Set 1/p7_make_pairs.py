"""
Understand:
- Make pairs in the list, nums, such that each elemeent in nums belongs to exactly
one pair where each element in pair are equal). 
- If nums can be divided into n pairs where the length of list is 2*n, then return True. 
- False otherwise.

Plan:
- Create a dictionary including all num in nums with their occurences as values for num.
- Return True if all values for each num is even. False if odd. 
- Also false if number of pairs are not half of the number of elements in nums. (Doesn't matter)
** Reversed boolean values in checking.

Implement:
"""

def divideList(nums):
    dict = {} 

    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    for value in dict.values():
        if value % 2 != 0:
            return False
    
    return True

nums = [3,2,3,2,2,2]
print(divideList(nums))