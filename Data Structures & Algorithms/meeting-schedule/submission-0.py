"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        new_intervals = []

        for interval in intervals:
            new_intervals.append((interval.start, interval.end))

        new_intervals.sort()

        for i in range(1, len(new_intervals)):
            cur_start, _ = new_intervals[i]
            _, prev_end = new_intervals[i-1]

            if cur_start < prev_end:
                return False
        
        return True