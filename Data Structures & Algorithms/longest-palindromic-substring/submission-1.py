class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_sub = ""
        max_sub_len = 0

        for i in range(len(s)):
            left = i
            right = len(s)-1

            while left <= right:
                sub_str = s[left: right+1]
                if sub_str == sub_str[::-1]:
                    str_length = right-left+1
                    if str_length > max_sub_len:
                        max_sub_len = str_length
                        max_sub = sub_str
                    break
                
                right -= 1
        
        return max_sub