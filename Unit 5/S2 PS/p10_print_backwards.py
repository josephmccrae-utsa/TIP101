"""
Understand:
- Write function print_reverse() that takes in tail of doubly linked list as parameter.
- Function should print out the values of the linked list i nreverse order, each
separated by a space.
Plan:
- Creaet a Node variable, current, initalized to tail.
- Iterate through doubly linked list via while loop, while current exists.
    - Every iteration, print current.value + " "
    - Initialize current to current.prev.
Implement:
"""
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def print_reverse(tail):
    current = tail

    while current:
        print(current.value, end=" ")
        current = current.prev
    pass


poliwrath = Node("Poliwrath")
poliwhirl = Node("Poliwhirl")
poliwag = Node("Poliwag")

poliwag.next = poliwhirl
poliwhirl.prev = poliwag
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath)