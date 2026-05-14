class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        def backtrack(index):

            subset_sum = sum(subset)

            if subset_sum == target:
                res.append(subset.copy())
                return
            
            if subset_sum > target or index >= len(nums):
                return

            subset.append(nums[index])
            backtrack(index)
            subset.pop()

            backtrack(index+1)
        
        res = []
        subset = []
        backtrack(0)
        return res
