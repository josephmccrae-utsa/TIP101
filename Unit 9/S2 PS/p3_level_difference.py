from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

"""
Understand:
- Write function level_difference(), with parameter root of binary tree.
- Return level difference between the sums of the valus of the nodes in the
even levels and the odd levels.
Plan:
- Use BFS iterative approach to traverse the binary tree.
- Sum each node value from the the odd levels and the same with the even 
levels.
- Return the difference between the odd levels and the even levels.  
Implement:
"""

def min_depth(root):
    if not root:
        return None
    
    odd_sum = 0
    even_sum = 0
    level = 1

    queue = deque()
    queue.append(root)

    while queue:
        popped = queue.popleft()

        if level == 1 or level % 2 == 1:
            odd_sum += popped.val
        elif level % 2 == 0:
            even_sum += popped.val

        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
        level += 1 
    print("Odd: " + str(odd_sum))
    print("Even: " + str(even_sum))
    return odd_sum - even_sum

root = TreeNode(6, TreeNode(3, TreeNode(5)), TreeNode(8, TreeNode(4, TreeNode(1), TreeNode(7, TreeNode(2, None, TreeNode(3))))))
print(min_depth(root))