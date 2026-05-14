class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(index):

            res.append(arr[:])

            for i in range(index+1, len(nums)):
                arr.append(nums[i])
                backtrack(i)
                arr.pop()
        
        arr = []
        backtrack(-1)
        
        return res