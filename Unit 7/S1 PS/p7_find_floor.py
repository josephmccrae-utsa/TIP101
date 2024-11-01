"""
Understand:
- Write function find_floor() with parameters: lst and x.
- Function should return the index of the floor of x.
- The floor of x is the largest element in the array smaller than or 
equal to x. 
- No floor? Return -1.
Plan:
- Create variable, floor, initialized at -1 to represent the index of floor.
- Iterate through the indeces of lst via for loop. 
    - Compare each value of lst to x, initializing floor to the index of 
    value if the value is lesser or equal to x.
    - If value is greater than x, return floor
Implement:
"""
def find_floor(lst, x):
    floor = -1

    for index in range(0, len(lst)):
        if lst[index] <= x:
            floor = index
        else:
            return floor
    
lst = [1, 2, 8, 10, 11, 12, 19]
print(find_floor(lst, 3))