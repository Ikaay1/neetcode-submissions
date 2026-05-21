class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def has_cycle(node, parent):

            if node in explored:
                return True
            
            explored.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                if has_cycle(neighbor, node):
                    return True
            
            return False

        graph = defaultdict(set)
        n = 0

        for node1, node2 in edges:
            graph[node1].add(node2) 
            graph[node2].add(node1)
            n = max(n, node1, node2)

        for i in range(len(edges)-1, -1, -1):
            node1, node2 = edges[i]
            explored = set()
            graph[node1].remove(node2)
            graph[node2].remove(node1)
            if not has_cycle(1, -1) and len(explored) == n:
                return edges[i]
            graph[node1].add(node2)
            graph[node2].add(node1)
        
