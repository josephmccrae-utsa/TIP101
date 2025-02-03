class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right
    
root = TreeNode(10)
child_one = TreeNode(4)
child_two = TreeNode(6)

root.left = child_one
root.right = child_two

print(root.val)
print(root.left.val)
print(root.right.val)