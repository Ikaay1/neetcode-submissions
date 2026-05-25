from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def dp(index, last):
            if index == len(nums):
                return 0
            
            res = dp(index+1, last)

            if nums[index] > last:
               res = max(res, 1 + dp(index+1, nums[index]))
            
            return res
        
        return dp(0, -float("inf"))