def per(key, ans=100):
    global maxV

    if ans <= maxV:
        return

    if key >= N:
        maxV = ans
        return

    for i in range(N):
        if visited[i]:
            visited[i] = False
            per(key + 1, ans * lst[key][i])
            visited[i] = True


for tc in range(1, 1 + int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            lst[y][x] /= 100
    visited = [True for _ in range(N)]
    maxV = 0
    per(0)
    print(f'#{tc} {maxV:.6f}')
