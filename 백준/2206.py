delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def req(x, y, flag, c):
    c += 1

    if x == M - 1 and y == N - 1:
        print(c)
        return c

    if flag:
        for dx, dy in delta:
            ifx, ify = x + dx, y + dy
            if 0 <= ifx < N and 0 <= ify < M and visited[ify][ifx]:
                visited[ify][ifx] = False
                if base_lst[ify][ifx] == 1:
                    req(ifx, ify, False, c)
                else:
                    print(ifx, ify, c)
                    req(ifx, ify, flag, c)
    else:
        for dx, dy in delta:
            ifx, ify = x + dx, y + dy
            if 0 <= ifx < M and 0 <= ify < N and visited[ify][ifx]:
                visited[ify][ifx] = False
                if base_lst[ify][ifx] == 0:
                    req(ifx, ify, False, c)


N, M = map(int, input().split())
base_lst = [list(map(int, list(input()))) for _ in range(N)]
visited = [[True for _ in range(M)] for _ in range(N)]

visited[0][0] = False
req(0, 0, True, 0)
