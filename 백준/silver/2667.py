'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

'''
from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
base_lst = [list(map(int, input())) for _ in range(N)]
visited = [[True for _ in range(N)] for _ in range(N)]

for y in range(N):
    for x in range(N):
        if base_lst[y][x] == 0:
            visited[y][x] = False
cnt = 0
ans = []
for y in range(N):
    for x in range(N):
        if base_lst[y][x] == 1:
            cnt += 1
            tmp = 1
            q = deque([[y, x]])
            base_lst[y][x] = 0
            visited[y][x] = False

            while q:

                go_y, go_x = q.popleft()
                for dy, dx in delta:
                    if_y, if_x = go_y + dy, go_x + dx
                    if 0 <= if_y < N and 0 <= if_x < N and visited[if_y][if_x]:
                        tmp += 1
                        visited[if_y][if_x] = False
                        if base_lst[if_y][if_x] == 1:
                            base_lst[if_y][if_x] = 0
                            q.append([if_y, if_x])

            ans += [tmp]
print(cnt)
ans.sort()
for i in ans:
    print(i)
