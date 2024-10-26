"""
Understand:
- Write function find_content_children() that takes in the greed list g and
the cookie size list s as paramaters and maximizes the number of content
children.
- A child is content if s[j] >= g[i], meaning the cookie size will satisfy
the child. If s[j] < g[i] the child will not be content.
Plan:
- Create counter, content, initialized at 0.
- Create child pointer, i, and cookie pointer, j, and initialize at 0.
- Increment through the list of children via child_pointer and for loop.
- Increment through cookie list via cookie counter and while loop until
s[j] >= g[i], if found, increment content.
- Return content. 

New plan:
- Sort each list. 
- Create coutner, content, for each content child, initiialzed at 0.
- Create pointers for both child and cookie list, initialized at 0.
- Increment using a while loop until child and cookie list has completed.
- If s[cookie_pointer] >= g[child_pointer], increment all variables.
- Otherwise, increment cookie_pointer. 
- Return content

Implement:
"""
def find_content_children(s, g):
    s.sort()
    g.sort()
    
    content = 0 # Unnecessary
    cookie_pointer, child_pointer = 0, 0

    while(child_pointer < len(g) and cookie_pointer < len(s)):
        if(s[cookie_pointer] >= g[child_pointer]):
            content += 1
            cookie_pointer += 1
            child_pointer += 1
        else:
            cookie_pointer += 1
    return content # Or return child_pointer
    pass


g = [1,3,2]
s = [1,3,1]
print(find_content_children(s, g))

g = [1,1]
s = [2,2,2]
print(find_content_children(s, g))
