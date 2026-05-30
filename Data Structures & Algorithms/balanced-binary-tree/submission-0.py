# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def is_balanced(root):

            if not root:
                return True, 0

            left_balanced, left_height = is_balanced(root.left)
            right_balanced, right_height = is_balanced(root.right)

            if not left_balanced or not right_balanced or not (-1 <= left_height - right_height <= 1):
                return False, -1
            
            return True, 1 + max(left_height, right_height)
        
        return is_balanced(root)[0]
            
