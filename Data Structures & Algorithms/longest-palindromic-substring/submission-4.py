class Solution:
    def longestPalindrome(self, s: str) -> str:

        def get_odd(i):
            left = i-1
            right = i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1

            return left, right
        
        def get_even(i):
            left = i
            right = i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1

            return left, right
        
        max_sub = ""
        max_sub_len = 0

        for i in range(len(s)):
            
            
            odd_left, odd_right = get_odd(i)
            even_left, even_right = get_even(i)

            odd_length = odd_right - odd_left + 1
            even_length = even_right - even_left + 1

            if odd_length > even_length:
                if odd_length > max_sub_len:
                    max_sub_len = odd_length
                    max_sub = s[odd_left: odd_right+1]
            else:
                if even_length > max_sub_len:
                    max_sub_len = even_length
                    max_sub = s[even_left: even_right+1]
        
        return max_sub