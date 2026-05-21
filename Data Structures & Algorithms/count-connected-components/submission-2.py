class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def bfs(node):
            queue = deque([node])
            explored.add(node)
            visited = {node}

            while queue:
                cur_node = queue.popleft()

                for neighbor in graph[cur_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        explored.add(neighbor)
                        queue.append(neighbor)

        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2) 
            graph[node2].append(node1) 
        
        explored = set()
        connected_components = 0
        for node in range(n):
            if node in explored:
                continue
            
            bfs(node)
            connected_components += 1
        
        return connected_components