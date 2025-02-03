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
Plan:
- Check if the values of the left child of root and right child of root 
equal the value of root. 
Implement:
"""
def check_tree(root):
    # if(root.left.val + root.right.val == root.val):
    #     return True
    # else:
    #     return False
    return root.left.val + root.right.val == root.val

root = TreeNode(10, TreeNode(4), TreeNode(6))
print(check_tree(root))

root2 = TreeNode(5, TreeNode(3), TreeNode(1))
print(check_tree(root2))