class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictionary = {}

        #row checking
        for i in range(0,9):
            dictionary = {}
            for j in range(0,9):
                content = board[i][j]
                if content != '.':
                    if content in dictionary:
                        return False
                    else:
                        dictionary[content] = content

        
        #column checking
        for j in range(0,9):
            dictionary = {}
            for i in range(0,9):
                content = board[i][j]
                if content != '.':
                    if content in dictionary:
                        return False
                    else:
                        dictionary[content] = content

        #box checking
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                dictionary ={}
                for x in range(3):
                    for y in range(3):
                        content = board[i+x][j+y]
                        if content != '.':
                            if content in dictionary:
                                return False
                            else:
                                dictionary[content] = content
        return True
