"""
Understand:
- Write function sum_of_number_strings that takes in list of strings nums.
- Each string is actually an integer so the function would return the sum
of the strings as an integer.
*Likely will need to convert Strings into integers.

Plan:
- Create variable to contain the sum of the strings as integers.
- Iterate through the list of strings.
- Add each strings, casted as an integer, to the sum variable.
- Return the sum variable.

Implement:
"""

def sum_of_number_strings(nums):
    sum = 0
    if len(nums) < 1:
        return 0

    for num in nums:
        if num.isalnum():
            sum += int(num)
    
    return sum
    pass

nums = [" ", "10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

