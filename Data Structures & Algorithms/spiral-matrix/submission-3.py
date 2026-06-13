class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        end_row = len(matrix)
        end_col = len(matrix[0])
        res = []
        index = 0

        while index < end_row-index and index < end_col-index:

            for c in range(index, end_col-index):
                res.append(matrix[index][c])
            
            for r in range(index+1, end_row-index):
                res.append(matrix[r][end_col-index-1])
            
            for c in range(end_col-index-2, index, -1):
                res.append(matrix[end_row-index-1][c])
            
            for r in range(end_row-index-1, index, -1):
                res.append(matrix[r][index])
            
            index += 1
        
        while len(res) > end_row * end_col:
            res.pop()
        
        return res