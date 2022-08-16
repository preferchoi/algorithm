import numpy as np

for tc in range(1, 1 + int(input())):
    N = int(input())

    mapp = []

    for i in range(N):
        mapp.append([0] * N)

    go_x = [0, 1, 0, -1]
    go_y = [1, 0, -1, 0]
    x, y = 0, 0
    go = 0

    for i in range(1, N * N + 1):
        mapp[x][y] = i
        x += go_x[go]
        y += go_y[go]
        # print(x, y)
        if x < 0 or y < 0 or x >= N or y >= N or mapp[x][y] != 0:
            x -= go_x[go]
            y -= go_y[go]
            go = (go + 1) % 4
            x += go_x[go]
            y += go_y[go]

    mapp = np.words(mapp)
    print(mapp)
