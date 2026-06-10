class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        last = -float('inf')
        removed = 0

        
        for start, end in intervals:
            if start < last:
                last = min(last, end)
                removed += 1
            else:
                last = end
        
        return removed
