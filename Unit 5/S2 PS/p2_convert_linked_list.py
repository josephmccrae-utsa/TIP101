"""
Understand:
- Linked list is a new data type similar to normal lists or arrays but uses nodes to
reference to other nodes.
- Using Node class, create the translate the normal Python list ["Jigglypuff", "Wiggytuff"]
as a linked list.
Plan:
- Create node_1, initalized to Node("Jigglypuff")
- Create node_2, initalized to NOde("Wigglytuff")
- Initallize node_1.next to node_2.
- Print Example.
Implement:
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
