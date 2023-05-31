from collections import deque
from copy import deepcopy

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def go(deep):
    if deep == 3:
        global minV
        BFS()
        return

    for go_y in range(N):
        for go_x in range(M):
            if visited[go_y][go_x] and base_lst[go_y][go_x] == 0:
                visited[go_y][go_x] = False
                base_lst[go_y][go_x] = 1
                go(deep + 1)
                visited[go_y][go_x] = True
                base_lst[go_y][go_x] = 0


def BFS():
    global minV, ans
    tmp_lst = deepcopy(base_lst)
    if_q = deque(virus[:])
    cnt = 0
    while if_q:
        cnt += 1
        if cnt > minV:
            return cnt
        bfs_y, bfs_x = if_q.popleft()
        for dy, dx in delta:
            if_y, if_x = bfs_y + dy, bfs_x + dx
            if 0 <= if_y < N and 0 <= if_x < M and not tmp_lst[if_y][if_x]:
                tmp_lst[if_y][if_x] = 2
                if_q.append([if_y, if_x])

    if cnt < minV:
        minV = cnt
        ans = 0
        for i in tmp_lst:
            ans += i.count(0)
    return cnt


N, M = map(int, input().split())
base_lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[True for _ in range(M)] for _ in range(N)]

ideaV = 0
virus = []
for y in range(N):
    ideaV += base_lst[y].count(0)
    for x in range(M):
        if base_lst[y][x] == 2:
            virus += [[y, x]]

minV = len(virus) + ideaV
ans = 0
for y in range(N):
    for x in range(M):
        if base_lst[y][x] == 0:
            visited[y][x] = False
            base_lst[y][x] = 1
            go(1)
            base_lst[y][x] = 0

print(ans)
