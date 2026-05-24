from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(index, total):

            if total == amount:
                return 0

            if total > amount or index == len(coins):
                return float('inf')

            return min(1+dp(index, total + coins[index]), dp(index+1, total))
        
        res = dp(0, 0)

        if res == float('inf'):
            return -1

        return res