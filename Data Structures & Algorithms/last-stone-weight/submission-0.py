class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            largest = -heapq.heappop(heap)
            second_largest = -heapq.heappop(heap)

            diff = largest-second_largest
            if diff:
                heapq.heappush(heap, -diff)
        
        if not heap:
            return 0
        
        return -heap[0]
