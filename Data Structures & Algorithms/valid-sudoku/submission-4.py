class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(0,9):
            freq={}
            for j in range(0,9):
                if board[i][j]!='.':
                    freq[board[i][j]]=1+freq.get(board[i][j],0)
            for k in freq.values():
                if k>1:
                    return False

        for j in range(0,9):
            freq={}
            for i in range(0,9):
                if board[i][j]!='.':
                    freq[board[i][j]]=1+freq.get(board[i][j],0)
            for k in freq.values():
                if k>1:
                    return False
        for i in range(0,9,3):
            for  j in range(0,9,3):
                freq={}
                for k in range(0,3):
                    for l in range(0,3):
                        r=i+k
                        c=j+l
                        if board[r][c]!='.':
                            freq[board[r][c]]=1+freq.get(board[r][c],0)
                    for num in freq.values():
                        if num>1:
                            return False
        return True



