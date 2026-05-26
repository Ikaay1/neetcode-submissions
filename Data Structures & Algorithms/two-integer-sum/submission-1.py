class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = defaultdict(deque)

        for i, num in enumerate(nums):
            hashMap[num] = i

        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in hashMap and hashMap[other_num] != i:
                return [i, hashMap[other_num]]