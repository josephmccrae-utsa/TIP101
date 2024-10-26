"""
Nodes or rather linked lists:
A linked list is a new data type that, similar to a normal list or array, 
allows us to store pieces of data sequentially. The difference between a 
linked list and a normal list lies in how each element is stored in a 
computer's memory.

In a normal list, individual elements of the list are stored in adjacent 
memory locations according to the order they appear in the list. If we 
know where the first element of the list is stored, it's really easy to 
find any other element in the list.

In a linked list, the individual elements called nodes are not stored in 
sequential memory locations. Each node may be stored in an unrelated 
memory location. To connect nodes together into a sequential list, each 
node stores a reference or pointer to the next node in the list.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
    

# node_two = Node('b')
# node_one = Node('a', node_two)

		
# print(node_one.value) 
# print(node_one.next.value) 
# print(node_two.value)
# print(node_two.next) 


# node_4 = Node("Toad")
# node_3 = Node("Wario", node_4)
# node_2 = Node("Luigi", node_3)
# node_1 = Node("Mario", node_2)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

def print_linked_list(head):
	current = head
	
	while current:
		print(current.value, end="")
		if current.next != None:
			print(" -> ", end="")
		current = current.next
	
node_5 = Node('e')
node_4 = Node('d', node_5)	
node_3 = Node('c', node_4)
node_2 = Node('b', node_3)
node_1 = Node('a', node_2)



print_linked_list(node_1)


