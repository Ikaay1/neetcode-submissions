from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1
        
        for num in hashMap:
            if hashMap[num] == 1:
                return num