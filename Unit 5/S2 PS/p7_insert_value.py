"""
Understand:
- Write function ll_instert() that takes in head of linked list, value val, and index
i as parameters.
- Function should insert a new Node with value val at index i of linked list, then
return head of linked list.
- If i is greater than length of list, insert new node at end of the list.
Plan:
- Create Node variable, current, initialized to head.
- Create Node variable, insertion, inialized to Node(val)
- Iterate through linked list via for loop until index i (w/ ll_index to track indeces).
    - For every interation initalize current.next to current.
- Once ll_index equals index i, initailize insertion.next to current.next and 
current.next to insertion
-  
Implement:
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_insert(head, val, i):
    current = head
    insertion = Node(val)

    for index in range(0, i-1):
        if current.next:
            current = current.next
        
    
    insertion.next = current.next
    current.next = insertion
    if i == 0:
        return insertion
    else:
        return head

num4 = Node(9)
num3 = Node(12, num4)
num2 = Node(8, num3)
num1 = Node(3, num2)

head = num1
# linked list: 3 -> 8 -> 12 -> 9
ll_insert(head, 20, 3)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9
current = num1
while current:
    print(current.value)
    current = current.next
