"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        nodes_to_new_nodes = {}

        def get_nodes(node):
            if node in nodes_to_new_nodes:
                return

            nodes_to_new_nodes[node] = Node(node.val)

            for child in node.neighbors:
                get_nodes(child)

        def map_nodes(node):
            new_node = nodes_to_new_nodes[node]

            if node in mapped:
                return new_node
            
            mapped.add(node)

            for child in node.neighbors:
                new_node.neighbors.append(map_nodes(child))
            
            return new_node
        
        # def print_nodes(node):
        #     if node in printed_nodes:
        #         return

        #     for child in node.neighbors:
        #         printed_nodes[node.val].append(child.val)
        #         print_nodes(child)
        
        if not node:
            return node
        
        get_nodes(node)
        mapped = set()
        res = map_nodes(node)
        # printed_nodes = defaultdict(list)
        # print_nodes(nodes_to_new_nodes[node])
        # print(printed_nodes)
        return res
        