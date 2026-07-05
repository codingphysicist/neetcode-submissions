class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            freq={}
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                elif board[i][j] in freq:
                    freq[board[i][j]]+=1
                else:
                    freq[board[i][j]]=1
            for k in freq.values():
                if k>1:
                    return False
        for i in range(0,9):
            freq={}
            for j in range(0,9):
                if board[j][i]==".":
                    continue
                elif board[j][i] in freq:
                    freq[board[j][i]]+=1
                else:
                    freq[board[j][i]]=1
            for k in freq.values():

                if k>1:
                    return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                freq={}
                for k in range(0,3):
                    for l in range(0,3):
                        r=i+k
                        c=j+l
                        if board[r][c]==".":
                            continue
                        elif board[r][c] in freq:
                            freq[board[r][c]]+=1
                        else:
                            freq[board[r][c]]=1
                for m in freq.values():
                    if m>1:
                        return False
        return True           