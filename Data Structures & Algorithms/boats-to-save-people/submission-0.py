class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        
        unlimited boats
        each both carry at most 2 people (must be less than or equal to limit weight)

        output -> int

        [1, 3, 2, 3, 2] -> any order is possible
        [] -> 0
        [3], limit = 2 -> limit will always be >= a given person's weight

        minimum amount of boat -> each boat to carry as much people as possible
        
        [1,3,2,3,2], limit=3
        
        [1,3,2,3,2], limit=3
        [1,2,2,3,3]
        - I want to carry the most amount of people I can per trip (smallest weights first)
        """


        """
        [1,3,2,3,2]
        heap = [1,3,2,2,3]
        smallest = 1
        biggest = 2
        boats = 1

        heap = [2,3,3]
        smallest = 2
        biggest = 3
        boats = 2

        heap = [3,3]
        smallest = 3
        biggest = 3
        boats = 3

        heap = [3]
        smallest = 3
        biggest = 0
        boats = 4

        heap = []
        return 4

        [5,1,4,2]
        heap = [1,5,3,2]
        smallest = 1
        biggest = 2
        boats = 1

        heap = [3,5]
        smallest = 3
        biggest = 5
        boats = 1

        """
        # heap = []

        # for person in people:
        #     heapq.heappush(heap, person)
        
        # boats = 0
        # while heap:
        #     smallest = heapq.heappop(heap)
        #     if heap:
        #         biggest = heapq.heapop(heap)
        #     else:
        #         biggest = 0

        #     if smallest + biggest > limit:
        #         heapq.heappush(heap, biggest)
            
        #     boats += 1
        
        # return boats


        people.sort()
        left = 0
        right = len(people)-1
        boats = 0

        while left <= right:
            weight_of_both = people[left] + people[right]

            if weight_of_both <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            boats += 1
        
        return boats

