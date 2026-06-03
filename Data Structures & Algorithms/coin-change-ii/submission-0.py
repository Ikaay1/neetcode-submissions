from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(index, current_amount):

            if amount == current_amount:
                return 1
            
            if index == len(coins) or current_amount > amount:
                return 0
            
            return dp(index, current_amount+coins[index]) + dp(index+1, current_amount)
        
        return dp(0, 0)