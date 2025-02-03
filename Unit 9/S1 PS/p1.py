class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Understand:
- Write function, is_symmetric(), with parameter root of binary tree.
- Return True if the tree's left and right subtree are mirrors of each other.
- False otherwise.
Plan:
- Create a helper function, match_subtrees(), with parameters sub_left and sub_right.
    - Check case parent has not children, return True.
    - Chech case for parent having one child, return False
    - Check case if left value and right value are unequal, return False.

    *We want to compare the outer nodes from the left subtree and the right tree as well
    as the inner nodes of the left subtree and the right subtree.
    - Return match_subtrees(sub_left.left, sub_right.right) and match_subtrees(sub_left.right, sub_right.left)
    - 
Implement:
"""
def match_subtrees(sub_left, sub_right):
    if not sub_left and not sub_right:
        return True
    if not sub_left or not sub_right:
        return False
    if sub_left.val != sub_right.val:
        return False
    
    return match_subtrees(sub_left.left, sub_right.right) and match_subtrees(sub_left.right, sub_right.left) 



def is_symmetric(root):
    if not root:
        return None
    
    left_subtree = root.left
    right_subtree = root.right

    return match_subtrees(left_subtree, right_subtree)

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(root))

root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(root))

root = None
print(is_symmetric(root))
    
