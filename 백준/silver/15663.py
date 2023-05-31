def go(tmp, deep):
    if deep <= 0:
        print(*tmp)
        return
    pre = 0
    for i in range(N):
        if visited[i] and pre != N_list[i]:
            visited[i] = False
            go(tmp + [N_list[i]], deep - 1)
            visited[i] = True
            pre = N_list[i]


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
visited = [True] * N

go([], M)
