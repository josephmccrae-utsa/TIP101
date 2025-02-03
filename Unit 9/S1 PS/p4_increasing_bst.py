class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Understand:
- Write function, increasing_bst(), with parameter root of binary search tree.
- Rearrange the tree so that the leftmost node is the root and every node has only
one right child.
- Return root of modified tree.
Plan:
- Create helper function, inorder_traversal(), with parameters root and lst, to collect
all nodes of tree in order.
    - Recursion of left.
    - Append value of root to lst.
    - Recusion of right.
- With the sorted node vales, iterate through lst, initializing root to TreeNode(val),
and root = root.right
Implement:
"""
def inorder_traversal(root, lst):
    if not root:
        return
    inorder_traversal(root.left, lst)
    lst.append(root.val)
    inorder_traversal(root.right, lst)

def increasing_bst(root):
    lst = []
    inorder_traversal(root, lst)

    new_root = TreeNode(lst[0])
    current = new_root
    for i in range(1, len(lst)):
        current.right = TreeNode(lst[i])
        current = current.right
    
    return new_root

root = TreeNode(5, TreeNode(1), TreeNode(7))
new_root = increasing_bst(root)

while new_root:
    print(new_root.val)
    new_root = new_root.right