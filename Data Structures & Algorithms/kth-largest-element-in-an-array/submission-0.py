class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)
        
        while heap:
            num = heapq.heappop(heap)
            k -= 1

            if k == 0:
                return -num
        
        return -1