from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(index, sold):
            if index >= len(prices):
                return 0

            res = dfs(index+1, sold)
            if sold != -1:
                if prices[index] > sold:
                    res = max(res, prices[index] - sold + dfs(index+2, -1))
            else:
                res = max(res, dfs(index+1, prices[index]))
            
            return res
        
        return dfs(0, -1)
            