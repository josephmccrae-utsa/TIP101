class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Understand:
- Write function left_most() with paramater root of binary tree.
- Return the value of the left most node.
- Iterative!
Plan:
- Create node variable, current, initialized to root.
- Iterate through binary tree via while loop until root.next doesn't exist.
    - Initalize current to current.left
- Return current.val
Implement:
"""
def left_most(root):
    current = root
    
    while current.left:
        current = current.left
    
    return current.val
    pass

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(left_most(root))

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root))