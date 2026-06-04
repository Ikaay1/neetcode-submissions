class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum = -float('inf')
        cur_sum = 0

        for num in nums:
            cur_sum += num
            maximum = max(maximum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0
        
        return maximum