from pprint import pprint

N_list = [list(map(int, input().split())) for _ in range(5)]

shout = []
for _ in range(5):
    shout += list(map(int, input().split()))

cnt = 0
for i in shout:
    flag = 0
    cnt += 1

    # 그 칸을 지우는 2중 for 문
    for y in range(5):
        for x in range(5):
            if N_list[y][x] == i:
                N_list[y][x] = 0

    # 가로줄
    for y in range(5):
        if not sum(N_list[y]):
            flag += 1

    for y in range(5):
        tmp = 0
        for x in range(5):
            tmp += N_list[x][y]
        if not tmp:
            flag += 1

    tmp = 0
    for y in range(5):
        tmp += N_list[y][y]
    if not tmp:
        flag += 1

    tmo = 0
    for y in range(5):
        tmo += N_list[y][4 - y]
    if not tmo:
        flag += 1

    if flag == 3:
        break

print(cnt)
