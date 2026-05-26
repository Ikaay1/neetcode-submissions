class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = Counter(s)

        for char in t:
            s_map[char] -= 1
        
        for _, freq in s_map.items():
            if freq != 0:
                return False
        
        return True