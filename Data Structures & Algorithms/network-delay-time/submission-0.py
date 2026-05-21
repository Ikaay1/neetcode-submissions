class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        def dijkstra(node):

            heap = [(0, node)]
            visited = {}

            while heap:
                time, cur_node = heapq.heappop(heap)

                if cur_node in visited:
                    continue

                visited[cur_node] = time

                for neighbor_node, additional_time in graph[cur_node]:
                    new_time = time + additional_time
                    if neighbor_node not in visited or new_time < visited[neighbor_node]:
                        heapq.heappush(heap, (new_time, neighbor_node))
            
            return visited
        
        graph = defaultdict(list)

        for from_node, to_node, time in times:
            graph[from_node].append((to_node, time)) 

        visited = dijkstra(k)

        if len(visited) < n:
            return -1
        
        return max(time for _, time in visited.items())
