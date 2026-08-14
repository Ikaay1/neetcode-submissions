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

    def merge(self):


        print(self.booked_events)
        
        stack = SortedList()

        for event in self.booked_events:
            startTime, endTime = event

            if not stack or startTime > stack[-1][1]:
                stack.add(event)
            else:
                stack[-1][1] = endTime
        
        self.booked_events = stack

        # [(0, 5),(5, 6),(6, 10)]
        
    
    def book(self, startTime: int, endTime: int) -> bool:

        def find_if_opening(startTime, endTime):
            """
            [10, 20]
            [20, 30]
            """
            for event in self.booked_events:

                cur_event_startTime, cur_event_endTime = event

                if not((endTime <= cur_event_startTime) or ( startTime >= cur_event_endTime)):
                    return False
            
            return True


        is_opening = find_if_opening(startTime, endTime)

        if not is_opening:
            return False
        
        self.booked_events.add([startTime, endTime])
        self.merge()

        # O(m) -> n is not the number of events books
        #  -> number of merged events groups

        return True
    
    # binary search solution



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)