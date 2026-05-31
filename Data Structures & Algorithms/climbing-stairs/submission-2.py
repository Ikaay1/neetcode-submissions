from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dfs(steps):
            if steps >= n:
                return steps == n

            return dfs(steps+1) + dfs(steps+2)
        
        return dfs(0)