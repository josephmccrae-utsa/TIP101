"""
Understand:
- Write function listify_first_n() that takes in a head of a linked list 
and a non-negative integer n as parameters.
- Function returns a list of values of the first n nodes.
- If n is greater than the length of the linked list, return a list of the
values of all nodes in the linked list.

Plan:
- Create empty list, lst.
- Create Node variable, current, initialized to head.
- Iterate through linked list via for loop for n iterations.
    - Append current.value to lst.
    - If current.next, initalize current to current.next
- Return lst.
Implement:
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
    lst = []
    current = head

    for i in range(n):
        lst.append(current.value)

        if current.next:
            current = current.next
        else:
            break
    
    return lst

c = Node('c')
b = Node('b', c)
a = Node('a', b)

# linked list: a -> b -> c
head = a
lst = listify_first_n(head,2)
print(lst)

l = Node('l')
k = Node('k', l)
j = Node('j', k)

# linked list: j -> k -> l 
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)