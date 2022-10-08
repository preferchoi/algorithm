def go(tmp, deep):
    if deep <= 0:
        print(*tmp)
        return
    for i in range(N):
        go(tmp + [N_list[i]], deep - 1)


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
go([], M)
