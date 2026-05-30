# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import cache
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        @cache
        def is_sub(root, sub_root):

            if not sub_root and not root:
                return True
            
            if not sub_root or not root:
                return False

            res = False
            if root.val == sub_root.val:
                res = is_sub(root.left, sub_root.left) and is_sub(root.right, sub_root.right)
            
            res = res or is_sub(root.left, subRoot) or is_sub(root.right, subRoot)
            return res
        
        return is_sub(root, subRoot)