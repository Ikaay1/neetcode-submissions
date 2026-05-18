class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def get_neighbors(row, col):
            return [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

        def is_valid(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] != -1

        def get_shortest(row, col):

            queue = deque([(0, row, col)])
            visited = {(row, col)}

            while queue:
                steps, row, col = queue.popleft()

                if grid[row][col] == 0:
                    return steps

                for neighbor_row, neighbor_col in get_neighbors(row, col):
                    if is_valid(neighbor_row, neighbor_col) and (neighbor_row, neighbor_col) not in visited:
                        visited.add((neighbor_row, neighbor_col))
                        queue.append((steps+1, neighbor_row, neighbor_col))
            
            return grid[row][col]
        
        rows = len(grid)
        cols = len(grid[0])

        res = [[-2] * cols for row in range(rows)]

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == -1:
                    grid[row][col] == -1
                elif grid[row][col] == 0:
                    grid[row][col] == 0
                else:
                    grid[row][col] = get_shortest(row, col)