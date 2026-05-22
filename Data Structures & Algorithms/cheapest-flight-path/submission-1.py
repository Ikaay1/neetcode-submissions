class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for from_node, to_node, price in flights:
            graph[from_node].append((to_node, price))


        heap = [(0, src, 0)]
        visited = {src: 0}

        while heap:
            cost, airport, stops = heapq.heappop(heap)

            if airport == dst:
                return cost
            
            if stops > k:
                continue
            
            visited[airport] = cost
            
            for neighbor_airport, neighbor_cost in graph[airport]:
                new_cost = cost + neighbor_cost

                if neighbor_airport not in visited or new_cost < visited[neighbor_airport]:
                    heapq.heappush(heap, (new_cost, neighbor_airport, stops+1))
        
            # print(visited)
        return -1