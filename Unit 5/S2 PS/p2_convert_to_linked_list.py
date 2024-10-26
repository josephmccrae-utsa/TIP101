class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)