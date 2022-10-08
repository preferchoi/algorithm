'''
3
0 0 0
0 0 0
0 0 0

'''
from collections import deque

delta = [(0, 1), (1, 1), (1, 0)]
delta2 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
pipe = 0  # 0 = 가로, 1= 대각, 2 = 세로
N = int(input())
base_lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if base_lst[y][x] == 1:
            for dy, dx in delta2:
                if_y, if_x = y + dy, x + dx
                if 0 <= if_y < N and 0 <= if_x < N:
                    visited[if_y][if_x] = True

for y in range(N):
    for x in range(N):
        if visited[y][x]:
            base_lst[y][x] = 1

base_lst[0][0] = 1
base_lst[0][1] = 1

for i in base_lst:
    print(*i)

q = deque([[0, 0, 0, 1]])
cnt = 0
while q:
    pre_y, pre_x, go_y, go_x = q.popleft()

    key_y, key_x = go_y - pre_y, go_x - pre_x

    if key_y and not key_x:
        for dy, dx in delta[:2]:
            if_y, if_x = go_y + dy, go_x + dx
            if 0 <= if_y < N and 0 <= if_x < N:
                q.append([go_y, go_x, if_y, if_x])

    elif not key_y and key_x:
        for dy, dx in delta[1:]:
            if_y, if_x = go_y + dy, go_x + dx
            if 0 <= if_y < N and 0 <= if_x < N:
                q.append([go_y, go_x, if_y, if_x])

    else:
        for dy, dx in delta:
            if_y, if_x = go_y + dy, go_x + dx
            if 0 <= if_y < N and 0 <= if_x < N:
                q.append([go_y, go_x, if_y, if_x])

    print(q)
    if if_y == N-1 and if_x == N-1:
        cnt += 1

print(cnt)
