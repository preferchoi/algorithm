for tc in range(1, 11):
    N = int(input())
    N_list = [list(map(int, list(input()))) for _ in range(16)]

    s_y, s_x = 0, 0
    flag = 0
    for y in range(1, 15):
        for x in range(1, 15):
            if N_list[y][x] == 2:
                s_y, s_x = y, x
                flag = 1
                break
        if flag:
            break

    queue = [[s_y, s_x]]
    go = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    print(f'#{tc}', end=' ')
    while queue:
        y, x = queue.pop(0)
        for a, b in go:
            dy, dx = y + a, x + b
            if 0 <= dy < 16 and 0 <= dx < 16:
                if N_list[dy][dx] == 0:
                    N_list[dy][dx] = 1
                    queue.append([dy, dx])
                elif N_list[dy][dx] == 3:
                    flag = 0
                    break
        if not flag:
            print(1)
            break
    else:
        print(0)