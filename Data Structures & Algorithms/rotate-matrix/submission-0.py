class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        levels = n//2

        for row in range(levels):
            for col in range(n):
                other_row = n-row-1

                keep = matrix[row][col]
                matrix[row][col] = matrix[other_row][col]
                matrix[other_row][col] = keep

        for row in range(n-1):
            for col in range(row+1, n):
                keep = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = keep
        