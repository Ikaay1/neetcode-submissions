class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            cur_area = min(left_height, right_height) * (right-left)
            max_area = max(max_area, cur_area)

            if left_height < right_height:
                left += 1
            else:
                right -= 1
        
        return max_area
            