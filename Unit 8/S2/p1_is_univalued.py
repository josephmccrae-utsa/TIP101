class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

"""
Understand:
- Write function, is_univalued(), with parameters: root.
- Return True if the binary tree is uni-valued, False otherwise.
Plan:
- Use recursion to traverse through the binary tree, checking the root value
to it's children's values. If at any point, they differ, return False.
- Base Case: If not root, return None.
- Recursive Case:
    - If root.left, check values, then is_univalued(root.left)
    - If root.right, check values , then is_univalued(root.right)
Implement:
"""
def is_univalued(root):
    if not root:
        return None

    if root.left:
        if root.val == root.left.val:
            is_univalued(root.left)
        else:
            return False
    if root.right:
        if root.val == root.right.val:
            is_univalued(root.right)
        else:
            return False
    
    return True

root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
print(is_univalued(root))     

root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(2, None, TreeNode(1)))
print(is_univalued(root))           
