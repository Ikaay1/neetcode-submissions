class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = Counter(nums)

        heap = [(-freq, num) for num, freq in frequencies.items()]
        heapq.heapify(heap)
        k_frequent = []
        remaining = k

        while heap and remaining:
            freq, num = heapq.heappop(heap)
            k_frequent.append(num)
            remaining -= 1
        
        return k_frequent

