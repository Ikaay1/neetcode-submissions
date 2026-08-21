from functools import cache

class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Tn = Tn-1, Tn-2, Tn-3

        @cache
        def tribonacci(n):

            if n == 0:
                return 0
            
            if n <= 2:
                return 1

            return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

        """

        """
        n = 3
        """

        cache = [-1] * (n+1)
        
        def tribonacci_sequence(n):

            if n == 0:
                return 0
            
            if n <= 2:
                return 1
            
            if cache[n] != -1:
                return cache[n]

            tribonacci_for_n = tribonacci_sequence(n-1) + tribonacci_sequence(n-2) + tribonacci_sequence(n-3)
            cache[n] = tribonacci_for_n
            return tribonacci_for_n
        
        return tribonacci_sequence(n)
    