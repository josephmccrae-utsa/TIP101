

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)

# repeat_hello(5)
		
"""
Understand:
- Write function called reapeat_hello_iterative() with parameter n.
- Print 'Hello' n times.
Plan:
- Use a print statement including "Hello" and multiply it by n.
Implement:
"""
def repeat_hello_iterative(n):
	print("Hello\n" * n)

repeat_hello_iterative(5)