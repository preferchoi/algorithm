def go(tmp, deep):
    if deep <= 0:
        print(*tmp)
        return
    for i in range(N):
        if visited[i]:
            for j in range(i):
                visited[j] = False
            go(tmp + [N_list[i]], deep - 1)
            for j in range(i):
                visited[j] = True


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
visited = [True for _ in range(N)]

go([], M)
