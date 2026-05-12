# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def get_index(start, end, target):
            for i in range(start, end+1):
                if inorder[i] == target:
                    return i

        queue = deque(preorder)

        def dfs(start, end):

            if start >= end:
                return None

            target = queue[0]
            index = get_index(start, end, target)

            node = TreeNode(target)
            queue.popleft()
            node.left = dfs(start, index)
            node.right = dfs(index+1, end)

            return node
        
        return dfs(0, len(inorder))

            