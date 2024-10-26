"""
Understand:
- Create function is_circular() that takes in parameter head of the linked 
list.
- Return True if the linked list is circular and False otherwise.
- A circular list connect the first and last nodes.
Plan:
- Create variable current, initialized to head.
- Iterate through the linked list until current.next equals head:
    - If current.next == None, return False.
    - Initialize current to the next node in linked list.
- Return True. 
Implement:
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# def is_circular(head):
#     current = head

#     while current.next != head:
#         if current.next == None:
#             return False
#         current = current.next
    
#     return True

def is_circular(head):
    if not head:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1

print(is_circular(num1))

