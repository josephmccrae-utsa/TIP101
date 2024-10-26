class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next



def get_tail(head):
    current = head

    while current:
        current = current.next

        if current.next == None:
            tail = current
   
    return tail

# linked list: num1->num2->num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

head = num1
tail = get_tail(num1)
print(tail)



