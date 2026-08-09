class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find the first occurence of the letter - scan per row
        # once found check left, right, up, down for the next letter
        # repeat until the last letter
        # return true if all the letters where found
        # otherwise, false
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c , i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i]!= board[r][c] or board[r][c] == '#'):
                return False
            
            #mark current visited 
            board[r][c] = "#"
            res = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
            
       