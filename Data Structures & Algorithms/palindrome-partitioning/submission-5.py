from functools import cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(string):
            return string == string[::-1]
        
        @cache
        def dfs(index):

            if index == len(s):
                return [[]]

            if index == len(s)-1:
                return [[s[index]]]

            string = []
            res = []
            for i in range(index, len(s)):
                string.append(s[i])

                if is_palindrome(string):
                    for arr in dfs(i+1):
                        res.append(["".join(string)] + arr)
            
            return res
        
        return dfs(0)
            

