'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29

'''
for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for N_y in range(N):
        for N_x in range(N):
            sumV = -N_list[N_y][N_x]

            for M_yx in range(- M + 1, M):
                if 0 <= N_y + M_yx < N:
                    sumV += N_list[N_y + M_yx][N_x]
                if 0 <= N_x + M_yx < N:
                    sumV += N_list[N_y][N_x + M_yx]

            if maxV < sumV:
                maxV = sumV

            sumV = -N_list[N_y][N_x]

            for M_yx in range(- M + 1, M):
                if 0 <= N_y + M_yx < N:
                    if 0 <= N_x + M_yx < N:
                        sumV += N_list[N_y + M_yx][N_x + M_yx]
                    if 0 <= N_x - M_yx < N:
                        sumV += N_list[N_y + M_yx][N_x - M_yx]

            if maxV < sumV:
                maxV = sumV

    print(f'#{tc} {maxV}')
