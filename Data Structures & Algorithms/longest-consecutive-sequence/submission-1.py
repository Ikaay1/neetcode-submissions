class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        used = set()
        res = 0

        for num in nums:
            if num in used:
                continue
            
            count = 0
            temp_num = num
            while temp_num not in used and temp_num in nums:
                used.add(temp_num)
                count += 1
                temp_num += 1
            
            temp_num = num-1
            while temp_num not in used and temp_num in nums:
                used.add(temp_num)
                count += 1
                temp_num -= 1
            
            res = max(res, count)
        
        return res
                