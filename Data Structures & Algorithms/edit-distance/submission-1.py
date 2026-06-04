from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def dp(index1, index2):

            if index1 == len(word1):
                return len(word2)-index2
            
            if index2 == len(word2):
                return len(word1)-index1

            res = dp(index1+1, index2+1)
            if word1[index1] != word2[index2]:
                return 1 + min(dp(index1+1, index2), res, dp(index1, index2+1))
            
            return res
        
        return dp(0, 0)