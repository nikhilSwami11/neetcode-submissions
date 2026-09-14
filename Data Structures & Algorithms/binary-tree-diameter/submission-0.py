# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = -float('inf')
        def get_height(node) -> int:
            nonlocal max_dia
            if not node:
                return 0
            
            left = get_height(node.left)
            right = get_height(node.right)

            max_dia = max(max_dia, left + right)
            return 1 + max(left,right)
        get_height(root)
        return max_dia
