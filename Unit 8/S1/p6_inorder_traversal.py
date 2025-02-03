class TreeNode():
     def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Understand:
- Write function inorder_traversal() with paramater root of binary tree.
- Return a list representing the inorder traversal of it's nodes values.
- Def: traverse the left subtree, then the current node, then the right subtree
Plan:
- Use helper function to keep track of list. Primarily code in this function,
and have the main inorder_traversal() function call it.
    - Base Case: if not current, return new_lst
    - Recursive Case:
        - inorder_traversal(current.left)
        - add current to lst
        - inorder_traveral(current.right)

- return lst.
Implement:
"""
def inorder_traverse(lst, root):
    new_lst = lst
    current = root

    if not current:
        return new_lst

    if current.left:
        inorder_traverse(new_lst, current.left)
    
    new_lst.append(current.val)

    if current.right:
        inorder_traverse(new_lst, current.right)

def inorder_traversal(root):
    lst = []
    current = root
    inorder_traverse(lst, current)
    return lst

        
    
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorder_traversal(root))

root = None
print(inorder_traversal(root))

root = TreeNode(1)
print(inorder_traversal(root))