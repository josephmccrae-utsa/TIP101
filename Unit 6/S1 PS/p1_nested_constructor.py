class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node = Node(4, Node(3, Node(2)))

current = node
while current:
    print(current.value)
    current = current.next