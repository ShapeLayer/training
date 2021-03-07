# Python => Time Over
# Pypy3 => Pass
from sys import stdin

sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]
zeros = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def able(i, j):
    arr = [i for i in range(1, 10)]

    for k in range(9):
        if sudoku[i][k] in arr:
            arr.remove(sudoku[i][k])
        if sudoku[k][j] in arr:
            arr.remove(sudoku[k][j])
    
    p = i // 3
    q = j // 3
    for a in range(3):
        for b in range(3):
            if sudoku[a+p*3][b+q*3] in arr:
                arr.remove(sudoku[a+p*3][b+q*3])
    
    return arr

printed = False
def dfs(x):
    global printed
    if printed:
        return
    if x == len(zeros):
        for arr in sudoku:
            print(' '.join(list(map(str, arr))))
        printed = True
        return
    else:
        (i, j) = zeros[x]
        possible = able(i, j)
        for n in possible:
            sudoku[i][j] = n
            dfs(x+1)
            sudoku[i][j] = 0
dfs(0)