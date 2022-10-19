'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9

'''
for tc in range(1, 1 + int(input())):
    sudoku_map = []
    ans_key = True
    N = 0
    for i in range(9):
        sudoku_map.append(list(map(int,input().split())))
    for i in sudoku_map:
        if sum(i) != 45:
            ans_key = False
    for i in range(9):
        N = 0
        for j in sudoku_map:
            N += j[i]
        if N != 45:
            ans_key = False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            N = 0
            N += sudoku_map[i][j] + sudoku_map[i+1][j] + sudoku_map[i+2][j]
            N += sudoku_map[i][j+1] + sudoku_map[i+1][j+1] + sudoku_map[i+2][j+1]
            N += sudoku_map[i][j+2] + sudoku_map[i+1][j+2] + sudoku_map[i+2][j+2]
            if N != 45:
                ans_key = False
    print(f'#{tc} {int(ans_key)}')