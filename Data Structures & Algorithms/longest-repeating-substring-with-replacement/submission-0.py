class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        indices = defaultdict(int)
        left = 0
        res = 0

        def is_valid(indices):
            to_remove = 0
            values = sorted(indices.values(), reverse=True)
            return sum(values[1:]) <= k


        for right in range(len(s)):
            char = s[right]
            indices[char] += 1

            while not is_valid(indices):
                indices[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res