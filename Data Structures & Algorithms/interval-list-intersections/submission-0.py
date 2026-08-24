class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        
        two pointer

        first_list_index = 0
        second_list_index = 0
        intersections = []

        while first_list_index < len(firstList) and second_list_index < len(secondList):

            first_start, first_end = firstList[first_list_index]
            second_start, second_end = secondList[second_list_index]

            intersection = get_intersections(first_start, first_end, second_start, second_end)
            intersections.append(intersection)

            if first_end < second_end:
                first_list_index += 1
            else:
                second_list_index += 1
        
        return intersections
        """

        """
        firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]

        first_list_index = 0
        second_list_index = 0
        """

        def get_intersections(first_start, first_end, second_start, second_end):

            new_start = max(first_start, second_start)
            new_end = min(first_end, second_end)

            if new_start > new_end:
                return []

            return [new_start, new_end]


        first_list_index = 0
        second_list_index = 0
        intersections = []

        # Time -> O(n) -> n is length of smallest list
        # Space -> O(m + n) -> 

        while first_list_index < len(firstList) and second_list_index < len(secondList):

            first_start, first_end = firstList[first_list_index]
            second_start, second_end = secondList[second_list_index]

            intersection = get_intersections(first_start, first_end, second_start, second_end)

            if intersection:
                intersections.append(intersection)

            if first_end < second_end:
                first_list_index += 1
            else:
                second_list_index += 1
        
        return intersections