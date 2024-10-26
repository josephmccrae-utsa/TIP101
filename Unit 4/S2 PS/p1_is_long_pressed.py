"""
Understand:
- Write function is_long_pressed() that takes in string name and string typed
as parameters. 
- Function should examine the typed characters in name and return True if
it was possible that name has some characters being long pressed. False otherwise.
- Use two-pointer approach to compare name and typed.
Plan:
- Create a pointer for each name and typed. (name_pointer, type_pointer) and
initialize at 0.
- Increment through name via pointer.
- If typed[typed_pointer] != name[name_pointer], return False
- While typed[typed_pointer] == name[name_pointer], increment typed_pointer
- Increment name_pointer when broken
- Everything good? Return True.
Implement:
"""
def is_long_pressed(name, typed):
    typed_pointer = 0

    for name_pointer in range(0, len(name)-1):
        if typed[typed_pointer] != name[name_pointer]:
            return False
        
        while typed[typed_pointer] == name[name_pointer]:
            typed_pointer += 1
        name_pointer += 1
    
    return True
    pass

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))