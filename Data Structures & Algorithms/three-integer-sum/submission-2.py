class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        nums_len = len(nums)
        triplets = set()

        for i in range(nums_len):
            left = i+1
            right = nums_len-1
            num = nums[i]

            while left < right:
                triplet_sum = nums[left] + nums[right] + num

                if triplet_sum == 0:
                    triplets.add((nums[left], nums[right], num))
                    left += 1
                    right -= 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return list(triplets)