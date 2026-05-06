class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        indices = {}
        left = 0
        res = 0

        for right in range(0, len(s)):
            char = s[right]

            if char in indices:
                while left < right and s[left] != char:
                    del indices[s[left]]
                    left += 1
                
                left += 1
            
            indices[char] = right
            res = max(res, right-left+1)
        
        return res