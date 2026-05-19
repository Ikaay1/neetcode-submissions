class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def get_valid_neighbors(row, col):
            neighbors = []

            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset

                if is_valid(new_row, new_col) and board[new_row][new_col] == "O":
                    neighbors.append((new_row, new_col))
            
            return neighbors

        def get_nodes(row, col):
            visited = {(row, col)}
            explored.add((row, col))
            queue = deque([(row, col)])
            nodes = [(row, col)]

            while queue:
                row, col = queue.popleft()

                for neighbor_row, neighbor_col in get_valid_neighbors(row, col):
                    if (neighbor_row, neighbor_col) not in visited:
                        visited.add((neighbor_row, neighbor_col))
                        explored.add((neighbor_row, neighbor_col))
                        nodes.append((neighbor_row, neighbor_col))
                        queue.append((neighbor_row, neighbor_col))
            
            return nodes

        def all_surrounded(nodes):
            
            for row, col in nodes:
                for row_offset, col_offset in directions:
                    new_row, new_col = row + row_offset, col + col_offset

                    if not is_valid(new_row, new_col):
                        return False
            
            return True

        

        explored = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        to_change = []
        for row in range(rows):
            for col in range(cols):

                if board[row][col] == "X" or (row, col) in explored:
                    continue

                nodes = get_nodes(row, col)
                if all_surrounded(nodes):
                    for node in nodes:
                        to_change.append(node)
        
        for row, col in to_change:
            board[row][col] = "X"
