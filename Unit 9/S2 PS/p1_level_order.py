from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

"""
Understnad:
- Write function, level_order(), with parameter root of binary tree.
- Return list of the level order traversal of it's nodes' values. 
Implement:
"""
def level_order(root):
    # If the tree is empty:
    if not root:
    # return an empty list
        return []

    # Create an empty queue using deque
    queue = deque()

    # Create an empty list to store the explored nodes
    lst = []

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    while queue:
        # Pop the next node off the queue (pop from the left side!)
        popped = queue.popleft()
        
        # Add the popped node to the list of explored nodes
        lst.append(popped)

        # Add each of the popped node's children to the end of the queue 
        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)

    # Return the list of visited nodes
    return lst

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
lst = level_order(root)
for node in lst:
    print(node.val)
