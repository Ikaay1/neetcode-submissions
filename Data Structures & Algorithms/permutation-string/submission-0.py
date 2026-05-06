class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freq = {}
        s1_freq = Counter(s1)
        
        for right in range(len(s2)):
            char = s2[right]
            freq[char] = freq.get(char, 0) + 1

            while right-left+1 > len(s1):
                freq[s2[left]] -= 1
                if not freq[s2[left]]:
                    del freq[s2[left]]
                left += 1
            
            if freq == s1_freq:
                return True
        
        return False