from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(index, sold):
            if index >= len(prices):
                return 0

            res = max(dfs(index+1, prices[index]), dfs(index+1, sold))
            if sold != -1 and prices[index] > sold:
                res = max(res, prices[index] - sold + dfs(index+2, -1))
            
            return res
        
        return dfs(0, -1)
            