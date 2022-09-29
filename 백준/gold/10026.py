from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

def go1(y, x, key):
    if 0 <= y < N and 0 <= x < N and lst[y][x] == key:
        lst[y][x] = 0
        go1(y + 1, x, key)
        go1(y, x + 1, key)
        go1(y - 1, x, key)
        go1(y, x - 1, key)


def go2(y, x, key=('R', 'G')):
    if 0 <= y < N and 0 <= x < N and mmm[y][x] in key:
        mmm[y][x] = 0
        go2(y + 1, x, key)
        go2(y, x + 1, key)
        go2(y - 1, x, key)
        go2(y, x - 1, key)


N = int(input())
lst = [list(input()) for _ in range(N)]
mmm = deepcopy(lst)

cnt1 = 0
cnt2 = 0

for Y in range(N):
    for X in range(N):
        if mmm[Y][X]:
            if mmm[Y][X] == 'B':
                go2(Y, X, [mmm[Y][X]])
            else:
                go2(Y, X)
            cnt2 += 1

for Y in range(N):
    for X in range(N):
        if lst[Y][X]:
            go1(Y, X, lst[Y][X])
            cnt1 += 1

print(cnt1, cnt2)
