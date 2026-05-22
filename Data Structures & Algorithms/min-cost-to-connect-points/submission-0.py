class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((manhattan_dist, j))
                graph[j].append((manhattan_dist, i))
        
        heap = [(0, 0)]
        visited = set()
        res = 0

        while heap:
            cost, index = heapq.heappop(heap)

            if index in visited:
                continue

            visited.add(index)
            res += cost

            for dist, neighbor in graph[index]:
                if neighbor not in visited:
                    heapq.heappush(heap, (dist, neighbor))
        
        return res