from functools import cache

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @cache
        def pow(n):
            if n == 1:
                return x
            
            num = 1
            if n % 2 == 1:
                num = x
            return num * pow(n//2) * pow(n//2)
        
        if n == 0:
            return 1
        
        if n < 0:
            return 1/pow(-n)
            
        return pow(n)