"""
Understand:
- Using Node class, write function ll_replace that takes a head of a linked 
list and two values, orignal and replacement as parameters.
- Function updates any node with value original to have value replacement.
Plan:
- Create Node variable, current, intialized to head.
- Iterate through linked list via while loop during current.next != None.
- If current.value is original, initialize current.value to replacement.

Implement:
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
    current = head

    while current:
        if current.value == original:
            current.value = replacement
        current = current.next
    pass

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print(num1.value)
print(num2.value)
print(num3.value)