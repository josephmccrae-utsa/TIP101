class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Understand:
- Write function left_most() with parameter root of binary tree.
- Return the value of the left most node in tree.
- Use Recursive Method.
Plan:
- Base Case: If root.left = None, return root.val.
- Recursive Case: If root.left, left_most(root.left)
Implement:
"""
def left_most(root):
    if not root:
        return None
    
    if not root.left:
       return root.val 
    
    left_most(root.left)
    
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(5))
print(left_most(root))

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root))

root = None
print(left_most(root))