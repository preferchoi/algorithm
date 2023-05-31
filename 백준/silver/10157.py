C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    N_list = [[0 for _ in range(C)] for _ in range(R)]

    go = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    key = 0
    y, x = -1, 0
    cnt = 1
    while True:
        y += go[key][0]
        x += go[key][1]
        if 0 <= y < R and 0 <= x < C and N_list[y][x] == 0:
            N_list[y][x] = cnt
            cnt += 1
        else:
            y -= go[key][0]
            x -= go[key][1]
            key += 1
            key %= 4
        if cnt == K + 1:
            print(x + 1, y + 1)
            break
