from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:
        
        """
        k count must be > 1
        n = 12
        2 ... 12

        2 -> 2

        def max_product(value_left):

            if value_left == 0:
                return 1
            
            if value_left < 2:
                return -inf
            
            maximum_prod = 1
            for num in range(2, value_left+1):
                maximum_prod = max(maximum_prod, num * max_product(value_left-num))
            
            return maximum_prod
        
        return max_product(n)
            

        12
        10
        8
        6
        4
        2
        """

        @cache
        def max_product(value_left):
            maximum_value = 0 if value_left == n else value_left
            for new_value in range(1, value_left):
                maximum_value = max(maximum_value, max_product(new_value) * max_product(value_left - new_value))
            
            return maximum_value
        
        return max_product(n)
