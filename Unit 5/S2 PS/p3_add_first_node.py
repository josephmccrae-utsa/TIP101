"""
Understand:
- Write function add_first() that takes in head of linked list and new_node from Node
class as paratmers.
- Function should insert new_node as the new head of the linked list. 
- Also return new_node.
Plan:
- Create Node variable current, initalized to Node head.
- Initialize new_node.next to current, thus creating the new header.
- Return new_node.
Implement:
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	current = head
	new_node.next = current
	
	return new_node


node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

