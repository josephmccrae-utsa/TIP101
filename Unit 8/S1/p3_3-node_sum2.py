class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Understand:
- Write function check_tree() with parameter root of binary tree.
- Return True if the value of root is equal to the sum of the values of its
children.
- False otherwise.
- Difference from previous problem is that that root may have have one or no
children. It's even possible from root to not exist.
Plan:
- Establish case if root doesn't exist.
- Establish if left and right children exist, if so, initalize left and right
variables with values of children.
- Check if the sum of left and right equal the value of root. 
Implement:
"""
def check_tree(root):
    if not root:
        return False
    
    right, left = 0, 0

    if root.left:
        left = root.left.val
    if root.right:
        right = root.right.val
    
    return left + right == root.val
    pass

root = TreeNode(10, TreeNode(10))
print(check_tree(root))

root = TreeNode(5, TreeNode(3), TreeNode(2))
print(check_tree(root))

root = TreeNode(5, None, TreeNode(2))
print(check_tree(root))

root = None
print(check_tree(root))