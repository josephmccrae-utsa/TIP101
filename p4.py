class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Understand:
- Write function left_most() with paramater root of binary tree.
- Return the value of the left most node.
- RECURSIVE!
Plan:
- Base Case: If not root, return None
- Recursive Case: If root.left, return left_most(root.left)
- Return root.val
Implement:
"""
def left_most(root):
    if not root:
        return None
    
    # if root.left:
    #     return left_most(root.left)
    
    # return root.val

    if not root.left:
        return root.val
    else:
        return left_most(root.left)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(left_most(root))

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root))