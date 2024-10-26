class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		

"""
Understand:
- Write function add_first() that takes parameter head of a linked list and
new_node from Node class as parameters.
- Function should insert new_node as the new head of linked_list. 
- Returnes new_node.
- Head of a linked list is the first element in the linked list.
Plan:
- Initialize new_node.next to head
- Return new_node.
Implement:
"""

def add_first(head, new_node):
	new_node.next = head
	return new_node

# Problem 2 linked list.
node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)


