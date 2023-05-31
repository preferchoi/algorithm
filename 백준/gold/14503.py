from collections import deque

Y, X = map(int, input().split())
q = deque([list(map(int, input().split()))])
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
base_lst = [list(map(int, input().split())) for _ in range(Y)]
visited = [[True for _ in range(X)] for _ in range(Y)]

cnt = 0

while q:
    y, x, go = q.popleft()
    visited[y][x] = False
    for d_go in range(3, -1, -1):
        if_y, if_x = y + delta[(go + d_go) % 4][0], x + delta[(go + d_go) % 4][1]
        if not base_lst[if_y][if_x] and visited[if_y][if_x]:
            q.append([if_y, if_x, (go + d_go) % 4])
            break

    else:
        if_y, if_x = y + delta[(go + 2) % 4][0], x + delta[(go + 2) % 4][1]
        if not base_lst[if_y][if_x]:
            q.append([if_y, if_x, go])

sumV = 0
for i in visited:
    sumV += X - sum(i)
print(sumV)
