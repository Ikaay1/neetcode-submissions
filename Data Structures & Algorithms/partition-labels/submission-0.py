class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        left = 0
        freq = Counter(s)
        current = {}
        res = []

        for right in range(len(s)):
            char = s[right]
            if not current:
                res.append(right-left)
                left = right
                current[char] = freq[char]-1
            else:
                if char in current:
                    current[char] -= 1
                else:
                    current[char] = freq[char]-1
                
            if not current[char]:
                del current[char]
        
        res.append(len(s)-left)

        return res[1:]