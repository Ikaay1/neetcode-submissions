class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def rows_valid():
            for row in range(rows):
                seen = set()
                for col in range(cols):
                    value = board[row][col]
                    if value == ".":
                        continue
                    if value in seen:
                        return False
                    seen.add(value)
            
            return True
        
        def columns_valid():
            for col in range(cols):
                seen = set()
                for row in range(rows):
                    value = board[row][col]
                    if value == ".":
                        continue
                    if value in seen:
                        return False
                    seen.add(value)
            
            return True
        
        def sub_boxes_valid():

            for row in range(0, rows, 3):
                for col in range(0, cols, 3):
                    seen = set()
                    for inner_row in range(row, row+3):
                        for inner_col in range(col, col+3):
                            value = board[inner_row][inner_col]
                            if value == ".":
                                continue
                            if value in seen:
                                return False
                            seen.add(value)
            
            return True
        
        def is_nums_valid():
            for row in range(rows):
                for col in range(cols):
                    value = board[row][col]
                    if value == ".":
                        continue
                    value = int(value)
                    if not (1 <= value <= 9):
                        return False
            
            return True


        rows = cols = 9

        if not is_nums_valid():
            return False

        return rows_valid() and columns_valid() and sub_boxes_valid()