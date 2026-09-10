# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        """
        
        def delete_leaves(node):

            if not node.left and node.right:
                if node.val == target:
                    return None
                else:
                    return node
            
            node.left = delete_leaves(node.left)
            node.right = delete_leaves(node.right)

            if not node.left and node.right:
                if node.val == target:
                    return None
                else:
                    return node

        3
            3
        3

        delete_node(3) -> None
        3.left = delete_node(None) -> None
        3.right = delete_node(3) -> None
                    2nd3.left = delete_node(3) -> None
                    2nd3.right = delete_node(None) -> None
        
        """
        def new_leaf(node):
            if node.val == target:
                return None
            else:
                return node

        def delete_leaves(node):

            if not node:
                return node

            if not node.left and not node.right:
                return new_leaf(node)
            
            node.left = delete_leaves(node.left)
            node.right = delete_leaves(node.right)

            if not node.left and not node.right:
                return new_leaf(node)
            
            return node
        
        return delete_leaves(root)
        