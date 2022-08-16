for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())

    N_list = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for N_y in range(N - M + 1):
        for N_x in range(N - M + 1):
            sumV = 0
            for M_y in range(M):
                for M_x in range(M):
                    sumV += N_list[N_y + M_y][N_x + M_x]
            if maxV < sumV:
                maxV = sumV
    print(f'#{tc} {maxV}')
