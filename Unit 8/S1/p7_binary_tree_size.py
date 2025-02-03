class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

"""
Understand:
- Write function size() with parameter root of binary tree.
- Return the number of nodes in binary tree.
Plan:
- Traverse through binary tree, counting each node that occurs.
- Use helper function traverse_count() to keep track of the number of cases.
- Base Case: If not current, return 0.
- Recurseive Case:
    - If current.left, traverse_count(count, current)
    - If current.right, traverse_count(count, current)
Implement:
"""
def traverse_count(count, root):
    num_nodes = count 
    current = root

    if not current:
        return num_nodes
    
    num_nodes += 1

    if current.left:
        return 1 + traverse_count(num_nodes, current.left)
    
    if current.right:
        return 1 + traverse_count(num_nodes, current.right)
    
    return num_nodes



def size(root):
    count = 0
    current = root

    return traverse_count(count, current)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(size(root))

root = None
print(size(root))
    