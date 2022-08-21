'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7

'''

N = int(input())
M = int(input())
N_list = [[False for _ in range(N + 1)] for _ in range(N + 1)]
visited_list = [False for _ in range(N + 1)]

for i in range(M):
    start, end = map(int, input().split())
    N_list[start][end] = True
    N_list[end][start] = True

stack = [1]

while stack:
    start = stack.pop()
    if not visited_list[start]:
        for i in range(N+1):
            if N_list[start][i]:
                stack.append(i)
    visited_list[start] = True

cnt = sum(visited_list) - 1
print(cnt)