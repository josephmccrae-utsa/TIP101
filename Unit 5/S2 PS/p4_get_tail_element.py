"""
Understand:
- Write function get_tail() that will take in parameter head of a linked list.
- Function should print out value of the tail (last element) of the list.
- If the list is emplty (head is None), return None
Plan:
- Initialize Node variable current to head.
- Iterate through linked list as long as current is not None.
- If current.next is not None, initializee current to current.next. Else 
print the value of current.
- If empty linked list, retur None
Implment:
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def linked_size(head, n):
    current = head
    

    for value in range(1, n+1):
        new_node = Node(current.value+1)
        current.next = new_node
        current = current.next
        print(current.value)
    return current.value
    
    pass


def get_tail(head):
    current = head

    if current is None:
        return None
    
    while current.next is not None:
        # if current.next is not None:
        #     current = current.next
        # else:
        #     return current.value
        current = current.next
    return current.value

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

# linked list: num1->num2->num3
head = num1
tail = get_tail(num1)
print(tail)

linked_size(num1, 20)