class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = set()

        def backtrack(index):

            res.add(tuple(sorted(arr)))

            for i in range(index+1, len(nums)):
                arr.append(nums[i])
                backtrack(i)
                arr.pop()
        
        arr = []
        backtrack(-1)
        
        return [list(arr) for arr in res]