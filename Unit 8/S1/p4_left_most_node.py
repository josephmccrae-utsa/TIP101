class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Understand:
- Write function left_most() with parameter root of binary tree.
- Return the value of the left most node in tree.
Plan:
- Establish case if binary tree doesn't exist.
- Iterate through binary tree until root.left doesn't exist.
    - Each iteration, initialze root with root.left
- Return root.val
Implement:
"""
def left_most(root):
    if not root:
        return None
	
    while root.left:
        root = root.left
    
    return root.val

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(5))
print(left_most(root))

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root))

root = None
print(left_most(root))