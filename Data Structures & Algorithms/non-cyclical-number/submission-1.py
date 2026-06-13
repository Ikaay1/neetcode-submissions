class Solution:
    def isHappy(self, n: int) -> bool:

        def is_one(n):
            new_n = 0
            str_n = str(n)

            for char in str_n:
                int_char = int(char)

                new_n += int_char ** 2
            
            return new_n, new_n == 1
        
        seen = set()

        while n not in seen:
            seen.add(n)
            n, is_non_cyclic = is_one(n)
            if is_non_cyclic:
                return True
        
        return False