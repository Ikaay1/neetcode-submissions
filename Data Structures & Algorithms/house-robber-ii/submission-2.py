from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index, first):
            if (index >= len(nums)-1 and first) or (index >= len(nums) and not first):
                return 0

            return max(nums[index] + dp(index+2, first), dp(index+1, first))

        return max(dp(1, False), nums[0] + dp(2, True))