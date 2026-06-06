class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        first, second, third = target
        has_first = False
        has_second = False
        has_third = False

        for cur_first, cur_second, cur_third in triplets:

            if cur_first > first or cur_second > second or cur_third > third:
                continue

            if cur_first == first:
                has_first = True
            if cur_second == second:
                has_second = True
            if cur_third == third:
                has_third = True
        
        return has_first and has_second and has_third