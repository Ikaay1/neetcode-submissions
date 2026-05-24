from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dp(index):
            if index == len(s):
                return 1
            
            string = ""
            res = 0
            for i in range(index, len(s)):
                char = s[i]
                string += char

                if int(string) > 26 or string == "0":
                    break
                
                res += dp(i+1)
            
            return res
        
        return dp(0)
                