class TreeNode():
     def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

"""
Understand:
- Write function, insert(), with parameters: root, key, value
- The function should insert a new node with the given key and value into
the tree.
- Return the new root.
- Tree is sorted by key. If a node with the given key exists, update it's 
value with the new value.
Plan:
- Binary Search Method via Binary Trees.
    - First check if the root's key is the target key, if so, update root.val.
    - Check if key is lesser the the root.key, returning recursively root.left
    - Return recursive root.right.
- IF we find that the key is greater or lesser than root.key, initalize a new
node with key and value, depending if greater or lesser.
Implement:
"""
def insert(root, key, value):
    current = root
    # Update Case
    if current.key == key:
        current.val = value
    
    if key < current.key:
        if current.left:
            return insert(current.left, key, value)
        else:
            current.left = TreeNode(key, value)
    else:
        if current.right:
            return insert(current.right, key, value)
        else:
            current.right = TreeNode(key, value)
    
    return root

root = TreeNode(10,  TreeNode(5, TreeNode(1), TreeNode(6)), TreeNode(15))
insert(root, 9, "Naruto")
# print(root.key)
    
