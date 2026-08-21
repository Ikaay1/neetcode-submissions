from functools import cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        triangle be empty?? -> return 0

        def smallest_path_sum(parent_index, child_index):

            if parent_index == len(nums):
                return 0

            return triangle[parent_index][child_index] + min(smallest_path_sum(parent_index+1, child_index), smallest_path_sum(parent_index+1, child_index+1))
        """

        """
        triangle = [
            [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
        ]

        smallest_path_sum(0, 0)
            2 + min(smallest_path_sum(1, 0), smallest_path_sum(1, 1))
        """

        @cache
        def smallest_path_sum(parent_index, child_index):

            if parent_index == len(triangle):
                return 0

            return triangle[parent_index][child_index] + min(smallest_path_sum(parent_index+1, child_index), smallest_path_sum(parent_index+1, child_index+1))

        return smallest_path_sum(0, 0)
