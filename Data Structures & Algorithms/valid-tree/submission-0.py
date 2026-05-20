class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def has_cycles(node, parent):

            if node in visited:
                return True
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if has_cycles(neighbor, node):
                    return True
            
            return False
        
        visited = set()
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        if has_cycles(0, None):
            return False
        
        return len(visited) == n
            
