class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum = -float('inf')
        cur_sum = 0

        for num in nums:
            cur_sum += num

            if cur_sum < 0:
                cur_sum = 0
                continue
                
            maximum = max(maximum, cur_sum)
        
        if maximum == -float('inf'):
            return max(nums)
        
        return maximum