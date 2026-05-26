class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = defaultdict(deque)

        for i, num in enumerate(nums):
            hashMap[num].append(i)

        for i, num in enumerate(nums):
            hashMap[num].popleft()

            other_num = target - num
            if hashMap[other_num]:
                return [i, hashMap[other_num][0]]