"""
Understand:
- Write function find_last_node_in_cycle() that takes in parameter head of 
linked list.
- Function should returns the last node in the cycle. If no cycle, return
None.
Plan:
- If head or head.next are None, return None (Simply checking for empty node case or no cycle case)

- Create slow pointer, slow, initalized to head.
- Create fast pointer, fast, initialized to head.
- Create boolean variable, cycle, initalized to False.

- Iterate through linked list while fast and fast.next exist.
    - Initialize slow to the next node in linked list.
    - Initalize fast to the next next node in linked list.
    - If slow equals fast, initialize cycle to be true (as linked list has been determined to be a cycle).
- If cycle is False, return None.

- Initalize slow to be head of linked list again.
- Iterate through linked list while slow doesn't equal fast.
    - Initialize slow to next node in linked list.
    - Initalize fast to next node in linked list.
*Once loop ends, slow and fast will equal the first value in the cycle. 

- Create node variable, start, initalized to slow.
- Create node variable, end, initalized to start (slow).
- Iterate through linked list until end.next == start (meaning that the next node after the end node, is the start node of the cycle).
    - Initalize end to next node in linked list.
*Once loop ends, end will be initalized to the last value of the cycle in the linked list.
- Return end.
Implement:
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



def find_last_node_in_cycle(head):
    if not (head or head.next):
        return None
    
    slow = head
    fast = head
    cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle = True
            break
    if not cycle:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    start = slow
    end = start
    while end.next != start:
        end = end.next
    
    return end
    

    

    
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

print(find_last_node_in_cycle(num1).value)