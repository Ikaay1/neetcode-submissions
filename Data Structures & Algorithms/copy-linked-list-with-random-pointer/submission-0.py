"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def get_indices():
            temp = head
            index = 0
            indices = {}
            nodes = []

            while temp:
                indices[temp] = index
                nodes.append(temp)
                index += 1
                temp = temp.next
            
            return indices, nodes

        indices, nodes = get_indices()
        res = res_temp = Node(0)
        new_nodes = [None]*len(nodes)

        for i in range(len(nodes)):
            node = nodes[i]
            new_nodes[i] = Node(node.val)
        
        for i in range(len(new_nodes)):
            new_node = new_nodes[i]
            random_node = nodes[i].random
            if not random_node:
                continue
            random_index = indices[random_node]
            new_random_node = new_nodes[random_index]
            new_node.random = new_random_node
        
        res = res_temp = Node(0)
        for node in new_nodes:
            res_temp.next = node
            res_temp = res_temp.next
        
        return res.next

        
