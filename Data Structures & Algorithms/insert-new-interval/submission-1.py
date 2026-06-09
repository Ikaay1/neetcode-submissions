class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()

        merged_intervals = []

        for interval in intervals:
            start, end = interval
            if merged_intervals and start <= merged_intervals[-1][1]:
                new_start, possible_end = merged_intervals.pop()
                merged_intervals.append([new_start, max(end, possible_end)])
            else:
                merged_intervals.append(interval)
        
        return merged_intervals