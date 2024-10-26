"""
Understand:
*A doubly linked list also has a prev attribute that points to the Node before it!
- Recreate list ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list via
Node class
Plan:
- Initalize each element of list with:
    - value = element.
    - next = (if present) next element.
    - prev = (if present) previous element.
Implement:
"""
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
poliwrath = Node("Poliwrath")
poliwhirl = Node("Poliwhirl")
poliwag = Node("Poliwag")

poliwag.next = poliwhirl
poliwhirl.prev = poliwag
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl

print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)