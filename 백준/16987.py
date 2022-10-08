'''
3
1 100
8 5
3 5

'''


def go(n):
    pass


N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
visited = [True] * N
visited[0] = False
go(0)
print(visited)
