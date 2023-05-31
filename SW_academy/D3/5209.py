def dfs(idx, sumV):
    global ans
    if sumV >= ans:
        return
    if idx == N:
        ans = sumV
    for i in range(N):
        if visited[i]:
            visited[i] = False
            dfs(idx + 1, sumV + lst[idx][i])
            visited[i] = True


for tc in range(1, 1 + int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [True for _ in range(N)]
    ans = 10 ** 10
    dfs(0, 0)
    print(f'#{tc} {ans}')
