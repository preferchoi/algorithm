'''
5 5 3
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1

'''
from itertools import combinations
from collections import deque
from copy import deepcopy


def go(go_y, n):
    # 타게팅
    visited_bow = [[True] * M for _ in range(N)]

    q = deque([[go_y, n, 1]])
    while q:
        y, x, deep = q.popleft()
        # 그 위치에 적이 있으면 쏠 준비 하고 그만둬
        if tmp[y][x] == 1:
            return [y, x]
        # D 칸 이상 갔으면 그만둬
        if deep >= D:
            return

        # 눈 앞부터 한칸씩 보면서 쏠 거 찾음
        for dy, dx in delta:
            if_y, if_x = y + dy, x + dx
            if 0 <= if_y < N and 0 <= if_x < M and visited_bow[if_y][if_x]:
                q.append([if_y, if_x, deep + 1])
                visited_bow[if_y][if_x] = False

    return False


N, M, D = map(int, input().split())
base_lst = [list(map(int, input().split())) for _ in range(N)]

minV = N * M
how_many = 0
for i in base_lst:
    how_many += sum(i)

delta = [(0, -1), (-1, 0), (0, 1)]
for one, two, three in list(combinations(range(M), 3)):

    tmp = deepcopy(base_lst)
    shell_y = N - 1
    cnt = 0
    while shell_y >= 0:

        shoot_1 = go(shell_y, one)
        shoot_2 = go(shell_y, two)
        shoot_3 = go(shell_y, three)
        if shoot_1:
            tmp[shoot_1[0]][shoot_1[1]] = 0
        if shoot_2:
            tmp[shoot_2[0]][shoot_2[1]] = 0
        if shoot_3:
            tmp[shoot_3[0]][shoot_3[1]] = 0
        shell_y -= 1

    for i in tmp:
        cnt += sum(i)

    if minV > cnt:
        minV = cnt


print(how_many - minV)

'''
사거리 1
0 @ 0
0 X 0
0 0 0

사거리 2
0 0 @ 0 0
0 X X X 0
0 0 X 0 0
0 0 0 0 0

사거리 3
0 0 0 @ 0 0 0
0 X X X X X 0
0 0 X X X 0 0
0 0 0 X 0 0 0
0 0 0 0 0 0 0

사거리 4
0 0 0 0 @ 0 0 0 0
0 X X X X X X X 0
0 0 X X X X X 0 0
0 0 0 X X X 0 0 0
0 0 0 0 X 0 0 0 0
0 0 0 0 0 0 0 0 0

사거리 5
0 0 0 0 0 @ 0 0 0 0 0 
0 X X X X X X X X X 0
0 0 X X X X X X X 0 0
0 0 0 X X X X X 0 0 0
0 0 0 0 X X X 0 0 0 0
0 0 0 0 0 X 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0


6 5 2
1 0 1 0 1
0 1 0 1 0
1 1 0 0 0
0 0 0 1 1
1 1 0 1 1
0 0 1 0 0
& @ @ & @

X 0 X 0 X
0 X 0 X 0
X X 0 0 0
0 0 0 X X
X X 0 X X
0 0 X 0 0
& @ @ & @



'''
