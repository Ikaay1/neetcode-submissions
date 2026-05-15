class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack():
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return

            for i in range(len(nums)):
                if i not in hashSet:
                    permutation.append(nums[i])
                    hashSet.add(i)
                    backtrack()
                    permutation.pop()
                    hashSet.remove(i)
        
        hashSet = set()
        permutation = []
        permutations = []
        backtrack()
        return permutations