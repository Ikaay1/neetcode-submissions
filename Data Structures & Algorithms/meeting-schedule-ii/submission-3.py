"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        used_rooms = []
        rooms = free_rooms = 0

        for interval in intervals:

            while used_rooms and used_rooms[0] <= interval.start:
                heapq.heappop(used_rooms)
                free_rooms += 1

            if not free_rooms:
                rooms += 1
            else:
                free_rooms -= 1

            heapq.heappush(used_rooms, interval.end)
                
        
        return rooms
            
        