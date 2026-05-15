class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(index):
            if index >= len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index+1)
            subset.pop()

            temp_index = index + 1

            while temp_index < len(nums) and nums[temp_index] == nums[index]:
                temp_index += 1

            backtrack(temp_index)
        
        subset = []
        subsets = []
        nums.sort()
        backtrack(0)
        return subsets

