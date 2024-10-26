"""
Understand:
- Write function list_to_linked_list() that takes in list lst as parameter and 
converts it to linked list.
- Function should return head of the linked list.
Plan:
- Create Node variable, head, initialized to Node(lst[0]).
- Create Node variable, current, initialized to head.
- Iterate through indeces of lst, from 1 to length of lst, via for loop.
    - Initalize current.next to Node(lst[index]).
    - Initalize current to current.next.
- Return head.
Implement:
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    head = Node(lst[0])
    current = head

    for index in range(1, len(lst)):
        current.next = Node(lst[index])
        if current.next != None:
            current = current.next
    
    return head.value

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element!

    