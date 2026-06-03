from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(index, cur_total):

            if index == len(nums):
                if cur_total == target:
                    return 1
                return 0

            return dp(index+1, cur_total + nums[index]) + dp(index+1, cur_total - nums[index])
        
        return dp(0, 0)