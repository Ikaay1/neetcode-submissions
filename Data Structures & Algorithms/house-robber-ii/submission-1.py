from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index):
            if index >= len(nums):
                return 0

            return max(nums[index] + dp(index+2), dp(index+1))
        
        @cache
        def dp2(index):
            if index >= len(nums)-1:
                return 0

            return max(nums[index] + dp2(index+2), dp2(index+1))
        
        # print(dp(1), dp2(0))
        if len(nums) == 1:
            return nums[0]
            
        return max(dp(1), dp2(0))