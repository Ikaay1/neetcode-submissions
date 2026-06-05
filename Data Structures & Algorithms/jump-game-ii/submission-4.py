from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # @cache
        # def dp(index):

        #     if index == len(nums)-1:
        #         return 0

        #     res = float('inf')
        #     for i in range(index+1, min(len(nums), index + nums[index] + 1)):
        #         res = min(res, 1+dp(i))
            
        #     return res
        
        # return dp(0)

        index = res = 0
        while index < len(nums)-1:
            farthest = 0

            for i in range(index, min(len(nums), index+nums[index]+1)):
                farthest = max(farthest, nums[i]+i)
            
            if index + nums[index] >= len(nums)-1:
                return res + 1
            
            res += 2
            index = farthest
        
        return res
