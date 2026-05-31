from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dfs(steps):
            if steps == 0:
                return 1

            res = 0
            if steps > 0:
                res += dfs(steps-1)
            if steps > 1:
                res += dfs(steps-2)
            
            return res
        
        return dfs(n)