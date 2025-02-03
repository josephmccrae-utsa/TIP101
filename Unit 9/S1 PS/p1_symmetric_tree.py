class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Understand:
- Write function is_symmetric(), with parameter root.
- Return True if the tree's left and right subtrees are equal to eachother.
- False otherwise.
Plan:
- Traverse and compare each subtree's values to eachother. Use a helper 
function to keep track of each subtree (need to compare left and right side at
the same time)
- Create function, match_subtree(), with parameters left and right.
    - Check case that left and right don't exist, return True.
    - Check case that one subtree exists, return False.
    - Check if left and right values unequal, Return False
    - Use recursion traverse and continue comparing outer and inner subtrees.

- Return the helper function with the two subtrees
Implement:
"""
def match_subtrees(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    
    return match_subtrees(left.left, right.right) and match_subtrees(left.right, right.left)


def is_symmetric(root):
    left_tree = root.left
    right_tree = root.right

    return match_subtrees(left_tree, right_tree)


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(root))

root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(root))