from functools import cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        nums is distinct

        nums = [1] target = 5 -> return 0
        nums[i] >= 1?? -> True
        target >= 1 -> True
        not sorted
        a given num multiple times

        nums = [5,1,2,3] target = 6

        def get_combinations(current_sum):

            if current_sum == target:
                return 1
            
            if current_sum > target:
                return 0

            num_of_combinations = 0    
            for index in range(len(nums)):
                num_of_combinations += get_combinations(current_sum + nums[i])
            
            return num_of_combinations
        
        """

        """
        nums = [3,1,2], target = 4
        get_combinations(0)
            get_combinations(3) -> return 1
                get_combinations(6) -> return 0
                get_combinations(4) -> return 1
                get_combinations(5) -> return 0
            get_combinations(1)
            get_combinations(2)
        """

        """
        
        """
        @cache
        def get_combinations(current_sum):

            if current_sum == target:
                return 1
            
            if current_sum > target:
                return 0

            num_of_combinations = 0    
            for index in range(len(nums)):
                num_of_combinations += get_combinations(current_sum + nums[index])
            
            return num_of_combinations
        
        return get_combinations(0)