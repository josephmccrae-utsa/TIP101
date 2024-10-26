"""
Understand:
- Create function reverse() that takes in parameter head of linked list.
- Function should return the head once the linked list has been reversed (value-wise).
Plan:
- Create node variable, current, initalized to head.
- Create empty list, values.
- Iterate through linked list while current exists.
    - For each iteration, append value of current to list, values.
    - Initialize current to next node in linked list.

- Create node variable header, initialzed to current.
- Create variable index, initalized to the second-to-last index of values.
- Iterate through values from the end to the start index via variable index.
    - Initialize current.next to Node(values[index])
    - Initalize current to next node.
    - Decremeent index.
- Return header.
New Plan:
- Create node
Implement:
"""
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    values = []
    current = head

    while current.next:
        values.append(current.value)
        current = current.next

    header = current
    index = len(values)-1
    while index >= 0:
        current.next = Node(values[index])
        current = current.next
        index -= 1
    return header
    pass

linked_list = Node(1, Node(2, Node(3, Node(4))))

reversed_list = reverse(linked_list)
print(reversed_list.value)

# current = reversed_list
# while current:
#     print(current.value)
#     current = current.next