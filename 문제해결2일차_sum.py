'''
1
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
2 1 1 1
2 1 1 1
2 1 1 1
2 1 1 1

'''
for tc in range(1, 11):
    N = input()
    N_list = [list(map(int, input().split())) for _ in range(100)]
    N_len = len(N_list)
    maxV = 0

    for col in N_list:
        sum_col = 0
        for x in col:
            sum_col += x
        if sum_col > maxV:
            maxV = sum_col

    for y in range(N_len):
        sum_row = 0
        for x in range(N_len):
            sum_row += N_list[x][y]
        if sum_row > maxV:
            maxV = sum_row

    sum_ls = 0
    sum_rs = 0
    for y in range(N_len):
        sum_ls += N_list[y][y]
        sum_rs += N_list[y][N_len - y -1]
    if maxV < sum_ls:
        maxV = sum_ls
    if maxV < sum_rs:
        maxV = sum_rs

    print(f'#{tc} {maxV}')
