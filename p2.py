class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Understand:
- Write function check_tree() with parameter root of binary tree.
- Return True if the value of root is equal to it's two children.
- Otherwise, False.
Plan:
- Check if the value of the root is equal to the sum of the values of the
left child and the right child.
- Return if that's true.
Implement:
"""

def check_tree(root):
    # if root.val == root.left.val + root.right.val:
    #     return True
    # else:
    #     return False
    return root.val == root.left.val + root.right.val

    pass

root = TreeNode(10, TreeNode(4), TreeNode(6))
print(check_tree(root))

root = TreeNode(5, TreeNode(3), TreeNode(1))
print(check_tree(root))