'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2

'''
go = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (1, -1), (0, -1), (-1, -1)]
for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    lst = [[0 for _ in range(N)] for _ in range(N)]
    lst[N // 2][N // 2] = 2
    lst[N // 2 - 1][N // 2] = 1
    lst[N // 2 - 1][N // 2 - 1] = 2
    lst[N // 2][N // 2 - 1] = 1

    for i in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        lst[y][x] = color
        for dy, dx in go:
            if_y, if_x = y + dy, x + dx
            if 0 <= if_y < N and 0 <= if_x < N:
                if lst[if_y][if_x] != 0 and lst[if_y][if_x] != color:
                    q = []
                    for j in range(N):
                        find_y, find_x = if_y + dy * j, if_x + dx * j
                        if 0 <= find_y < N and 0 <= find_x < N:
                            if lst[find_y][find_x] == color:
                                for change_y, change_x in q:
                                    lst[change_y][change_x] = color
                                break
                            elif lst[find_y][find_x] == 0:
                                break
                            else:
                                q.append([find_y, find_x])
    b, w = 0, 0
    for y in lst:
        for x in y:
            if x == 1:
                w += 1
            if x == 2:
                b += 1
    print(f'#{tc} {w} {b}')

