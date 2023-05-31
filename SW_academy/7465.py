def go(n):
    global cnt
    if not visited[n]:
        return

    for i in lst[n]:
        if visited[i]:
            visited[i] = False
            go(i)
            visited[i] = True

    cnt += 1


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N + 1)]
    visited = [True for _ in range(N + 1)]
    visited[0] = False
    for _ in range(M):
        s, e = map(int, input().split())
        lst[s] += [e]
        lst[e] += [s]

    cnt = 0
    for i in range(N + 1):
        go(i)
    print(cnt)
