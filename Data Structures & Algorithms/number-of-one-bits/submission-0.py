class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # 5 = 2**2 + 2**0
        # 7 = 2**2 + 2**1 + 2**0

        one_bits = 0
        
        while n > 1:
            product = 1
            
            while product * 2 <= n:
                product *= 2
            
            one_bits += 1
            n -= product
        
        if n == 1:
            one_bits += 1

        return one_bits