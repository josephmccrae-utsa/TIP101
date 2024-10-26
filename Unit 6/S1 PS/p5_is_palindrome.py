"""
Understand:
- Create function is_palidrome() that takes in parameter head of linked list.
- Function should return True if values of linked list are palidromic, false otherwise.
- Use two-pointer technique. (Multiple Pass Technique)
- A palidrome is a term that is read the same backwards. In this case, the term is the 
values of the 
linked list.
Plan:
- Create emppty list, values.
- Create node variable, current.
- Iterate through nodes as long as current exists.
    - For every node, append the value of the node to values.
    - Initalize current to the next node of the linked list.

- Create start pointer, start, initialized to beginning index in values.
- Create end pointer, end, initialized to the last index in values.
- Once we have our list of values from the linked list, iterate through index of values 
using both pointers, start and end until start and end equal are equal or start > end.
    - If values[start] != values[end], return False.
    - Increment start, decrement end.
- Return True.
Implement:
"""
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
    values = []
    current = head

    while current:
        values.append(current.value)
        current = current.next
    
    start = 0
    end = len(values)-1

    while start != end and start < end:
        if values[start] != values[end]:
            return False
        start += 1
        end -= 1
    return True
    pass

linked_list = Node(1, Node(2, Node(1, Node(2, Node(1)))))

print(is_palindrome(linked_list))