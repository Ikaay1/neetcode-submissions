from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dfs(steps):
            if steps == n:
                return 1

            res = 0
            if steps < n:
                res += dfs(steps+1)
            if steps < n-1:
                res += dfs(steps+2)
            
            return res
        
        return dfs(0)