class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, word_index):

            if word_index == len(word):
                return True

            if row < 0 or row == len(board) or col < 0 or col == len(board[row]) or (row, col) in hashSet:
                return False

            if word[word_index] == board[row][col]:
                hashSet.add((row, col))
                res = dfs(row+1, col, word_index+1) or dfs(row-1, col, word_index+1) or dfs(row, col+1, word_index+1) or dfs(row, col-1, word_index+1)
                hashSet.remove((row, col))
                return res
            
            return False
        
        hashSet = set()

        res = False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    res = res or dfs(row, col, 0)
        
        return res
