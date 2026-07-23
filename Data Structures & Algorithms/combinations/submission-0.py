class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        are we guaranteed that k <= n -> yes
        [1, 2] -> [2, 1] are same: unique combinations by values in array
        output: list[list[int]]



        n = 3, k = 2
        1 2 3

        [1]
        []


        combination = []
        def get_combinations(index):

            if len(combination) == k:
                combinations.append(combination[:])
                return

            loop from index, n+1:
                combination.append(nums[index])
                get_combinations(i+1)
                combination.pop()
            
        get_combinations(0)
        """

        """
        Input: n = 3, k = 3
        1, 2, 3
        
        combination = []
        get_combinations(0)

        combination = [1]
        get_combinations(1)

        combination = [1, 2]
        get_combinations(2)

        combination = [1, 2]
        get_combinations(3)
        """
        def get_combinations(index):

            if len(combination) == k:
                combinations.append(combination[:])
                return

            for i in range(index, n+1):
                combination.append(i)
                get_combinations(i+1)
                combination.pop()
        
        combination = []
        combinations = []
        get_combinations(1)

        return combinations