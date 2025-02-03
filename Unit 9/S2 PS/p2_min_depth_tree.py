from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

"""
Understand:
- Write function, min_depth(), with parameter root of binary tree.
- Return the minimum depth of the tree.
- The minimum depth is the number of nodes along the shortest path from the 
root down to the nearest leaf node.
Plan:
- Use the iterative method, Breadth First Search of traversing a binary 
tree.
- If we find a leaf (no children), record it's level and compare if it's 
lesser than min (initialized to infinity).
Implement:
"""
def min_depth(root):
    if not root:
        return None
    
    min_lvl = float('inf')
    level = 0
    queue = deque()
    queue.append(root)

    while queue:
        level += 1 
        popped = queue.popleft()

        if not popped.left and not popped.right:
            if level < min_lvl:
                min_lvl = level

        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
    
    return min_lvl

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(min_depth(root))

root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print(min_depth(root))