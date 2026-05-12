# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0

        def dfs(start, end):
            nonlocal pre_idx

            if start >= end:
                return None

            target = preorder[pre_idx]
            index = indices[target]

            node = TreeNode(target)
            pre_idx += 1
            node.left = dfs(start, index)
            node.right = dfs(index+1, end)

            return node
        
        indices = {}

        for i in range(len(inorder)):
            indices[inorder[i]] = i

        return dfs(0, len(inorder))

            