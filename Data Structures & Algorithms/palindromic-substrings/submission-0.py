class Solution:
    def countSubstrings(self, s: str) -> int:
        def get_odd(i):
            left = i
            right = i
            palindromes = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1

            return palindromes
        
        def get_even(i):
            left = i
            right = i+1
            palindromes = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1

            return palindromes
        
        palindromes_count = 0

        for i in range(len(s)):
            
            odd_palindromes = get_odd(i)
            even_palindromes = get_even(i)

            palindromes_count += odd_palindromes + even_palindromes
        
        return palindromes_count