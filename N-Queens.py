"""
Given a chess board having  cells, you need to place N queens on the board in such a way that no queen attacks 
any other queen.



Code from GeekforGeeks
https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/


"""

N = int(input())

  
def printSolution(board): 
    for i in range(N): 
        for j in range(N-1): 
            print (board[i][j],end = ' ') 
        print(board[i][N-1])
  
  
def isSafe(board, row, col): 
    for i in range(col):
        if board[row][i] == 1: 
            return False
  
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    return True
  
def solveNQUtil(board, col): 
    if col >= N: 
        return True
  
    for i in range(N): 
        if isSafe(board, i, col): 
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True: 
                return True
            board[i][col] = 0  
    return False
  
def main(): 
    board = [x[:] for x in [[0] * N] * N]
    if solveNQUtil(board, 0) == False: 
        return False
    printSolution(board) 
    return True
  
if  __name__ == "__main__":
   main()  
  
