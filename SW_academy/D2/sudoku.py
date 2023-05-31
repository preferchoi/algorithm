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

T = int(input())

for test_case in range(1, T+1):
    list = []
    for i in range(9):
        list.append(input().split(" "))
    # print(list)
    g = 0 # 가로
    s = 0 # 세로
    d = 0 # 대각선
    for i in range(9):
        for j in range(9):
            list[i][j] = int(list[i][j])
    # print(list)

    # 가로줄 검증
    for i in range(9):
        g_list = []
        for j in range(9):
            g_list.append(list[i][j])
        g_list.sort()
        if g_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            g += 1

    if g != 9:
        print(f'#{test_case}', 0)
        continue

    for i in range(9):
        s_list = []
        for j in range(9):
            s_list.append(list[j][i])
        s_list.sort()
        if s_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            s += 1
    if s != 9:
        print(f'#{test_case}', 0)
        continue

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            d_list = []
            for k in range(3):
                for m in range(3):
                    d_list.append(list[i+k][j+m])
            d_list.sort()
            if d_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                d += 1
    if d != 9:
        print(f'#{test_case}', 0)
        continue

    print(f'#{test_case}', 1)