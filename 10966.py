'''
3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL


for tc in range(1, 1 + int(input())):
    map_y, map_x = map(int, input().split())
    world = [list(input()) for _ in range(map_y)]

    sumV = 0
    go = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for y in range(map_y):
        for x in range(map_x):
            if world[y][x] == 'L':
                queue = [[y, x, 0]]
                flag = 0

                while queue:
                    dy, dx, deep = queue.pop()
                    deep += 1
                    for a, b in go:
                        if_y, if_x = dy + a, dx + b
                        if 0 <= if_y < map_y and 0 <= if_x < map_x:
                            if world[if_y][if_x] == 'W':
                                sumV += deep
                                flag = 1
                                break
                            queue.append([if_y, if_x, deep])
                    if flag:
                        break

    print(f'#{tc} {sumV}')
'''
for tc in range(1, 1 + int(input())):
    map_y, map_x = map(int, input().split())
    world = [list(input()) for _ in range(map_y)]
    go = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for y in range(map_y):
        for x in range(map_x):
            if world[y][x] == 'W':
                world[y][x] = 0
            else:
                world[y][x] = 999
    for y in range(map_y):
        for x in range(map_x):
            if world[y][x] == 0:
                tmp = [[y, x, 0]]
                while tmp:
                    if_y, if_x, deep = tmp.pop()
                    deep += 1
                    for a, b in go:
                        dy, dx = if_y + a, if_x + b
                        if 0 <= dy < map_y and 0 <= dx < map_x and world[dy][dx] > deep:
                            world[dy][dx] = deep
                            tmp.append([dy, dx, deep])

    sumV = 0
    for i in world:
        sumV += sum(i)
    print(f'#{tc} {sumV}')
