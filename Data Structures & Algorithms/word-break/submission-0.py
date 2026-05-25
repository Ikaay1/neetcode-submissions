from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)

        @cache
        def dp(index, string):
            if index == len(s):
                if not string:
                    return True
                return False

            new_string = string + s[index]
            
            if new_string in wordDict:
                if dp(index+1, ""):
                    return True
            
            if dp(index+1, new_string):
                return True
            
            return False
        
        return dp(0, "")