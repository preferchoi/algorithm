'''
3
3 3 0 1
4 2 1 3
4 2 2 1


0 * 0 * 0 * 0 * 0
*   *   *   *   *
0 * 0 * 0 * 0 * 0
*   *   *   *   *
0 * 0 * 0 * 0 * 0
*   *   *   *   *
0 * 0 * 0 * 0 * 0
*   *   *   *   *
0 * 0 * 0 * 0 * 0


'''
# x, y, 시작방향, 세대
delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]
line = []

for i in range(5):
    if i % 2:
        line += [[0 for _ in range(5)]]
    else:
        line += [[0 for _ in range(4)]]

for i in range(int(input())):
    x, y, go, age = map(int, input().split())
    if go % 2:
        if go == 0:
            line[y][x] = 1
        else:
            line[y][x - 1] = 1
    else:
        if go == 1:
            line[y][x] = 1
        else:
            line[y - 1][x] = 1
    x += delta[go][1]
    y += delta[go][0]

for i in line:
    print(*i)
