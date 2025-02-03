class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Understand:
- Write function, binary_tree_paths(), with parameter root of binary tree.
- Return list of all root-to-leaf paths.
- Order of list doesn't matter.
Plan:
- Traverse through the tree recursively but in a pre-order fashion.
- Create a helper function, traverse_add_list(), with parameters root, path, paths.
    - With every traversal, add to the path.
    - Once we have reached a leaf, append the current path to paths list.
    - Not a leaf? Recursion.
Implement:
"""
def traverse_add_list(root, path, paths):
    if not root:
        return
    
    if path:
        path += "->" + str(root.val)
    else:
        path = str(root.val)

    if not root.left and not root.right:
        paths.append(path)
    else:
        traverse_add_list(root.left, path, paths)
        traverse_add_list(root.right, path, paths)


def binary_tree_paths(root):
    paths = []
    traverse_add_list(root, "", paths)
    return paths


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binary_tree_paths(root))

root = TreeNode(1)
print(binary_tree_paths(root))

                       

"""
[] -> [1] -> [1, 2] -> [1, 2, 5]
"""