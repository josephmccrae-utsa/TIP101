class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

"""
Understand:
- Write function, height(), with parameters: root.
- Return the height of a binary tree.
Plan:
- Use helper function, traverse_height(), with parameter root and height.
    - Initalize the height to the current level (starting at 1)
    - With each recursion, we will increase the level by one.
    - Base Case: If not root, return None
    - Recursive Case:
        - If root.left, traverse_height(root.left, level+1)
        - If root.right, traverse_height(root.right, level+1)
    - Return level

New PLAN:
- MAX!!!!
Implement:
"""
# def traverse_height(root, lvl, height=0):
#     level = lvl

#     if level > height:
#         height = level

#     if not root:
#         return None
    
#     if root.left:
#         return traverse_height(root.left, level+1)
#     if root.right:
#         return traverse_height(root.right, level+1)

#     return height

# def height(root):
#     return traverse_height(root, 1)

def height(root):
    if not root:
        return 0
    
    left = height(root.left)
    right = height(root.right)
    
    return max(left, right) + 1 # Add one for root node.


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(height(root))

root = TreeNode(4)
print(height(root))