class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""
Understand:
- Write function, min_diff_in_bst(), with parameters root of binary tree.
- Return the minimum difference between the values of any two different
nodes in the tree.
Plan:
- Create helper function, traverse_inorder(), with parameters root and lst, to collect
every node into a lst via inorder recursion.
    - Case if root is None, return.
    - Recursion through left.
    - Append the root value to lst
    - Recursion through right.
- After collecting node values into lst, compare the difference of each of them to the
minimum (initialized to infinity). If lesser, initialize minimum to the difference.
Implement:
"""
def traverse_inorder(root, lst):
    if root:
        traverse_inorder(root.left, lst)
        lst.append(root.val)
        traverse_inorder(root.right, lst)
        

def min_diff_in_bst(root):
    lst = []
    traverse_inorder(root, lst)
    
    minimum = float('inf')
    for index in range(0, len(lst)-1):
        dif = lst[index+1] - lst[index]

        if dif < minimum:
            minimum = dif

    return minimum
    
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(min_diff_in_bst(root))

root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(min_diff_in_bst(root))