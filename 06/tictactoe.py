def TicTacDraw(board):
    n = len(board)
    for i in range(n):
        a = ''
        for j in range(n):
            if board[i][j] == 0:
                a = a + 'O'
            if board[i][j] == 1:
                a = a + 'X'
            elif board[i][j] ==2:
                a = a + ' '
        a=' | '.join(a)
        print(' ' + a)
        if i < n - 1:
            print((4*n-1)*'-')    
if __name__ == '__main__':
    eg = [[0,1,2],[2,0,0],[1,1,2]]
    TicTacDraw(eg)