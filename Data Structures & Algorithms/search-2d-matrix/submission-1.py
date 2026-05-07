class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bin_search_arr(matrix):
            left = 0
            right = len(matrix)-1

            while left <= right:
                mid = (left+right)//2

                if matrix[mid][-1] < target:
                    left = mid + 1
                elif matrix[mid][0] > target:
                    right = mid - 1
                else:
                    return mid
            
            return -1
        
        def bin_search(arr):
            left = 0
            right = len(arr)-1

            while left <= right:
                mid = (left+right)//2

                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False
        
        index = bin_search_arr(matrix)

        if index == -1:
            return False
        
        return bin_search(matrix[index])
        
