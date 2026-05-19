class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def get_valid_neighbors(row, col):

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = []

            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset

                if is_valid(new_row, new_col) and heights[row][col] >= heights[new_row][new_col]:
                    neighbors.append((new_row, new_col))
            
            return neighbors

        def can_flow(row, col):
            
            seen_rows = {row}
            seen_cols = {col}
            visited = {(row, col)}
            queue = deque([(row, col)])

            while queue:
                row, col = queue.popleft()

                for neighbor_row, neighbor_col in get_valid_neighbors(row, col):
                    if (neighbor_row, neighbor_col) not in visited:
                        visited.add((neighbor_row, neighbor_col))
                        seen_rows.add(neighbor_row)
                        seen_cols.add(neighbor_col)
                        queue.append((neighbor_row, neighbor_col))
            
            return (0 in seen_rows and rows-1 in seen_rows) or (0 in seen_rows and cols-1 in seen_cols) or (0 in seen_cols and rows-1 in seen_rows) or (0 in seen_cols and cols-1 in seen_cols)


        res = []
        rows = len(heights)
        cols = len(heights[0])

        for row in range(rows):
            for col in range(cols):
                if can_flow(row, col):
                    res.append([row, col])
        
        return res