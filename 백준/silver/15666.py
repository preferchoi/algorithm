def go(tmp, deep):
    if deep <= 0:
        print(*tmp)
        return
    pre = 0
    for i in range(N):
        if visited[i] and pre != N_list[i]:
            for j in range(i):
                visited[j] = False
            go(tmp + [N_list[i]], deep - 1)
            for j in range(i):
                visited[j] = True
            pre = N_list[i]


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
visited = [True] * N

go([], M)
