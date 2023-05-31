'''
3 1
4 5 2

'''


def go(tmp, deep):
    if deep <= 0:
        print(*tmp)
        return
    for i in range(N):
        if visited[i]:
            for j in range(i + 1):
                visited[j] = False
            go(tmp + [N_list[i]], deep - 1)
            for j in range(i + 1):
                visited[j] = True


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
visited = [True for _ in range(N + 1)]
N_list.sort()

go([], M)
