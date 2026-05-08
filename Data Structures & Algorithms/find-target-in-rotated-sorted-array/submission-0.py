class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search(start, end):
            left = start
            right = end

            while left <= right:
                mid = (left + right)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        def get_first_index():
            left = 0
            right = len(nums)-1

            while left < right:
                mid = (left + right)//2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        first_index = get_first_index()
        first_half = bin_search(0, first_index)
        second_half = bin_search(first_index, len(nums)-1)
        if first_half != -1:
            return first_half
        elif second_half != -1:
            return second_half
        
        return -1