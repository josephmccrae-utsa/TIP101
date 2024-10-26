"""
Understand:
- Define function count_element that takes in parameters: Node head and val.
- Return the frequency of val in the linked list.
Plan:
- Create Node varaible, current, initialized to head.
- Create variable, count, to contain frequency.
- Iterate through linked list as long as current exists.
    - Check if current.value is val, incrementing count each time. 
- Return count.
Implement:
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def count_element(head, val):
    current = head
    count = 0

    while current:
        if current.value == val:
            count += 1
        current = current.next
    return count

linked_list = Node(3, Node(1, Node(2, Node(1))))

print(count_element(linked_list, 1))

"""
Time Complexity: O(n) b/c only one while loop depending on size of linked list.
Space Complexity: O(1) b/c storage of nodes depends on number of nodes in linked list and
the incrementing counter (irrelevant compared to size of linked list).
"""