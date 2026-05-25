class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def recurse(index, cur_sum):
            if cur_sum == total-cur_sum:
                return True
            
            if index == len(nums):
                return False

            if recurse(index+1, cur_sum + nums[index]) or recurse(index+1, cur_sum):
                return True
            
            return False
        
        total = sum(nums)
        return recurse(0, 0)
