class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_freq = Counter(tasks)
        max_heap = [(-freq, task) for task, freq in tasks_freq.items()]
        cycles = 0

        heapq.heapify(max_heap)

        while max_heap:
            new_heap = []
            for i in range(n+1):
                if max_heap:
                    freq, task = heapq.heappop(max_heap)
                    if abs(freq) > 1:
                        heapq.heappush(new_heap, (freq+1, task))
                    cycles += 1
                elif new_heap:
                    cycles += 1
            
            while new_heap:
                heapq.heappush(max_heap, heapq.heappop(new_heap))
        
        return cycles