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
- Root may not have 2 children!!!
Plan:
- Establish case if root doesn't exist.
- Establish case for if root doesn't havr both child, one or the other.
    - Return if the sum of 0 and value of root that does exist equals root value.
Implement:
"""

def check_tree(root):
    if not root:
        return False
    
    # if root.left and root.right:
    #     return root.val == root.left.val + root.right.val
    # if root.left and not root.right:
    #     return root.val == root.left.val
    # elif root.right and not root.left:
    #     return root.val == root.right.val
    # else:
    #     return 0

    left, right = 0, 0

    if root.left:
        left = root.left.val
    if root.right:
        right = root.right.val

    return root.val == left + right


root = TreeNode(10, TreeNode(10))
print(check_tree(root))

root = TreeNode(5, TreeNode(3), TreeNode(2))
print(check_tree(root))

root = TreeNode(5, None, TreeNode(2))
print(check_tree(root))

root = None
print(check_tree(root))