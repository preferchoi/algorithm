'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
INF = N ** 2
base_lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[INF for _ in range(N)] for _ in range(N)]
chick = []
home = []
for y in range(N):
    for x in range(N):
        if base_lst[y][x] == 2:
            chick.append([y, x])
        if base_lst[y][x] == 1:
            home.append([y, x])

setting = list(combinations(chick, M))

for i in setting:
    q = deque(i)
    for c_y, c_x in q:

    while q:

