class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        indices = defaultdict(int)
        left = 0
        res = 0

        def is_valid(right, left, max_freq):
            return (right-left+1) - max_freq <= k

        max_freq = 0
        for right in range(len(s)):
            char = s[right]
            indices[char] += 1
            max_freq = max(max_freq, indices[char])

            while not is_valid(right, left, max_freq):
                indices[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res