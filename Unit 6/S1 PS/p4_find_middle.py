class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next


"""
Understand:
- Create function, find_middle_element, that takes in head of linked list.
- Function should return the middle node of the linked list.
- Use slow-fast pointer technique!
Plan:
- Create slow pointer, slow, initialized at head.
- Create fast pointer, fast, initialized at head.
- Iterate through linked list while fast and fast.next exists.
    - Initialize slow to the next node.
    - Initialize fast to the next next node.
- Return the value of slow (The middle value as fast ended the loop when slow 
reached the middle).
Implement:
"""
def find_middle_element(head):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value

nodes = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(find_middle_element(nodes))

