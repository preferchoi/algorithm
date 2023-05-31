def go(tmp, deep):
    if deep <= 0:
        print(*tmp)
        return
    for i in base_lst:
        go(tmp + [i], deep - 1)


N, M = map(int, input().split())
base_lst = list(range(1, N + 1))
visited = [True for _ in range(N + 1)]

go([], M)
