T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    list = []
    for i in range(N):
        list.append([0]*N)
    arrow, i, j = 0, 0, 0
    for K in range(1, N*N+1):
        if arrow == 0:
            list[i][j] = K
            if j == N-1 or list[i][j+1] != 0:
                arrow = 1
                i += 1
                continue
            j += 1
        elif arrow == 1:
            list[i][j] = K
            if i == N-1 or list[i+1][j]:
                arrow = 2
                j -= 1
                continue
            i += 1
        elif arrow == 2:
            list[i][j] = K
            if j == 0 or list[i][j-1]:
                arrow = 3
                i -= 1
                continue
            j -= 1
        elif arrow == 3:
            list[i][j] = K
            if i == 0 or list[i-1][j] != 0:
                arrow = 0
                j += 1
                continue
            i -= 1

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(list[i][j], end=" ")
        print()

        # for t in range(int(input())):
        #     n = int(input())
        #     b = [[0] * n for _ in range(n)]
        #     l = 1
        #     dx = [1, 0, -1, 0]
        #     dy = [0, 1, 0, -1]
        #     r = c = d = 0
        #     while l <= n * n:
        #         b[r][c] = l
        #         nr = r + dy[d]
        #         nc = c + dx[d]
        #         l += 1
        #         if 0 <= nr < n and 0 <= nc < n and b[nr][nc] == 0:
        #             r, c = nr, nc
        #         else:
        #             d = (d + 1) % 4
        #         r += dy[d]
        #         c += dx[d]
        #
        # print('#{}'.format(t + 1))
        # for i in b: print(*i)