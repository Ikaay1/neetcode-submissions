from sortedcontainers import SortedList

class MyCalendar:
    
    def __init__(self):
        """
        
        startTime < endTime?? -> Guaranteed

        self.booked_events = SortedList -> [(2, 5), (5, 12)]

        book
            binary search to see if we have opening
            if we do, add the event
                then merge any "clashes"
                return True

            if we don't
                return False
        """

        self.booked_events = SortedList()

        # [(0, 5),(5, 6),(6, 10)]
        
    
    def book(self, startTime: int, endTime: int) -> bool:

        def find_if_opening(startTime, endTime):
            """
            [10, 20]
            [20, 30]
            """
            # for event in self.booked_events:

            #     cur_event_startTime, cur_event_endTime = event

            #     if not((endTime <= cur_event_startTime) or ( startTime >= cur_event_endTime)):
            #         return False
            
            # return True

            left = 0
            right = len(self.booked_events)-1

            while left <= right:

                mid = (left + right)//2
                mid_start_time, _ = self.booked_events[mid]

                if mid_start_time == startTime:
                    return False
                elif mid_start_time < startTime:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if right >= 0:
                right_start_time, right_end_time = self.booked_events[right]
                if not((endTime <= right_start_time) or ( startTime >= right_end_time)):
                    return False
            
            if right + 1 < len(self.booked_events):
                right_start_time, right_end_time = self.booked_events[right+1]
                if not((endTime <= right_start_time) or ( startTime >= right_end_time)):
                    return False
            
            return True


        is_opening = find_if_opening(startTime, endTime)

        if not is_opening:
            return False
        
        self.booked_events.add([startTime, endTime])

        # O(m) -> n is not the number of events books
        #  -> number of merged events groups

        return True
    
    # binary search solution



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)