'''
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
1 0 0 0 0 0 1 0
1 0 1 1 1 0 1 0
1 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1

'''
for tc in range(1, 1 + int(input())):
    y, x = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(y)]

    maxV = 0
    for i in range(y):
        row = 0
        for j in range(x):
            if N_list[i][j] == 1:
                row += 1
            else:
                if maxV < row:
                    maxV = row
                row = 0
        else:
            if maxV < row:
                maxV = row

    for i in range(x):
        col = 0
        for j in range(y):
            if N_list[j][i] == 1:
                col += 1
            else:
                if maxV < col:
                    maxV = col
                col = 0
        else:
            if maxV < col:
                maxV = col

    print(f'#{tc} {maxV}')