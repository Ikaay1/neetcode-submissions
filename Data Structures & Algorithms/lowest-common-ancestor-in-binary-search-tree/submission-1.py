# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root):

            if not root:
                return None

            if ((root.val > p_val or root.val > q_val) and (root.val < p_val or root.val < q_val)) or (root.val == p_val or root.val == q_val):
                return root
            if root.val > p_val:
                print("entered", root.val)
                return dfs(root.left)
            if root.val < p_val:
                return dfs(root.right)

        p_val = p.val
        q_val = q.val

        return dfs(root)