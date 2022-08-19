for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    N_list_90 = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            N_list_90[y][x] = N_list[x][y]

    for y in range(N):
        for x in range(N - M + 1):
            if x == 0:
                if N_list[y][x:M + 1] == [1] * M + [0]:
                    cnt += 1
                if N_list_90[y][x:M + 1] == [1] * M + [0]:
                    cnt += 1

            elif x == N - M:
                if N_list[y][x - 1: N] == [0] + [1] * M:
                    cnt += 1
                if N_list_90[y][x - 1: N] == [0] + [1] * M:
                    cnt += 1

            else:
                if N_list[y][x - 1:x + M + 1] == [0] + [1] * M + [0]:
                    cnt += 1
                if N_list_90[y][x - 1:x + M + 1] == [0] + [1] * M + [0]:
                    cnt += 1

    print(f'#{tc} {cnt}')
