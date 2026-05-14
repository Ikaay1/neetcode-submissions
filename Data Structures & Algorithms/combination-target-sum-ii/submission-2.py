class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, subset_sum):

            if subset_sum == target:
                res.add(tuple(subset))
                return
            
            if subset_sum > target or index >= len(candidates):
                return
            
            candidate = candidates[index]
            subset.append(candidate)
            backtrack(index+1, subset_sum+candidate)
            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
                
            backtrack(index+1, subset_sum)
        
        candidates.sort()
        subset = []
        res = set()
        backtrack(0, 0)

        return [list(subset) for subset in res]
