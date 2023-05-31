def go(tmp, deep, pre):
    if deep <= 0:
        print(*tmp)
        return
    for i in base_lst:
        if i >= pre:
            go(tmp + [i], deep - 1, i)


N, M = map(int, input().split())
base_lst = list(range(1, N + 1))
visited = [True for _ in range(N + 1)]

go([], M, 0)
