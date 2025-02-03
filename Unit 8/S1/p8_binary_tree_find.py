class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


"""
Understand:
- Write function, find(), with parameter root and value.
- Function should return True if a node in the binary tree has value in the tree.
- False otherwise. 
- Tree is balanced.
Plan:
- Use recursion function, traverse_match() to traverse through the tree.
    - Check if the value of the node matches the given target value.
    - Base Case: If current.val = value, return True
    - Recursive Case:
        - If current.left, find(current.left)
        - If current.right, find(current.right)
- Otherwise, return False.
Implement:
"""
def traverse_match(root, value):
    target = value
    current = root
    
    if not current:
        return False
    
    if current.val == target:
        return True 
        
    return traverse_match(current.left, target) or traverse_match(current.right, target)
        


def find(root, value):
    if traverse_match(root, value):
        return True
    
    return False

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(find(root, 5))
