def go(node, sumV):
    global ans
    if sumV > ans:
        return
    if node == N:
        ans = sumV
        return
    for i in range(N + 1):
        if lst[node][i] and visited[i]:
            visited[i] = False
            go(i, sumV + lst[node][i])
            visited[i] = True


for tc in range(1, 1 + int(input())):
    N, E = map(int, input().split())
    lst = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited = [True for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        lst[s][e] = w
    ans = 10 * N
    go(0, 0)
    print(f'#{tc} {ans}')
