class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # find distances for each point in a min heap
        # pop first k smallest

        def get_distance(x, y):
            return math.sqrt(x**2 + y**2)

        distances = []

        for i in range(len(points)):
            x, y = points[i]
            distance = get_distance(x, y)

            heapq.heappush(distances, (distance, x, y))
        
        freq = k
        closest_points = []

        while freq and distances:
            distance, x, y = heapq.heappop(distances)
            closest_points.append([x, y])
            freq -= 1
        
        return closest_points