class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# node = TreeNode(10, 4, 6)

# root = TreeNode(10)
# left = TreeNode(4)
# right = TreeNode(6)
# root.left = left
# root.right = right

root = TreeNode(10, TreeNode(4), TreeNode(6))


print(root.val)
print(root.left.val)
print(root.right.val)