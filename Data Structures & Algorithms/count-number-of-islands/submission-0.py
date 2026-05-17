class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def get_neighbors(row, col):
            return [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

        def is_valid(neighbor_row, neighbor_col):
            return neighbor_row >= 0 and neighbor_row < rows and neighbor_col >= 0 and neighbor_col < cols
            
        def mark_connections(row, col):
            queue = deque([(row, col)])

            while queue:
                row, col = queue.popleft()

                for neighbor_row, neighbor_col in get_neighbors(row, col):
                    if is_valid(neighbor_row, neighbor_col) and grid[neighbor_row][neighbor_col] == "1":
                        grid[neighbor_row][neighbor_col] = "0"
                        queue.append((neighbor_row, neighbor_col))

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    mark_connections(row, col)
                    islands += 1
        
        return islands