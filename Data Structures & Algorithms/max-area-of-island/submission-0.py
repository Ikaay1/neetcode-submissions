class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def get_neighbors(row, col):
            return [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

        def is_valid(neighbor_row, neighbor_col):
            return neighbor_row >= 0 and neighbor_row < rows and neighbor_col >= 0 and neighbor_col < cols
            
        def mark_connections(row, col):
            queue = deque([(row, col)])
            grid[row][col] = 0
            area = 1

            while queue:
                row, col = queue.popleft()

                for neighbor_row, neighbor_col in get_neighbors(row, col):
                    if is_valid(neighbor_row, neighbor_col) and grid[neighbor_row][neighbor_col] == 1:
                        grid[neighbor_row][neighbor_col] = 0
                        queue.append((neighbor_row, neighbor_col))
                        area += 1
            
            return area

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, mark_connections(row, col))
        
        return max_area