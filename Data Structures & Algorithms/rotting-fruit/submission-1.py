class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        def get_neighbors(row, col):
            return [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

        queue = deque([])
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        minutes = -1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for neighbor_row, neighbor_col in get_neighbors(row, col):
                    if is_valid(neighbor_row, neighbor_col) and grid[neighbor_row][neighbor_col] == 1:
                        grid[neighbor_row][neighbor_col] = 2
                        queue.append((neighbor_row, neighbor_col))
                
            minutes += 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return max(0, minutes)