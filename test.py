def go(n, a, b):
    print(n, a, b)
    if n < 1:
        return

    cnt_y = -1
    for y in range(0, n * 3, n):
        cnt_x = -1
        cnt_y += 1
        for x in range(0, n * 3, n):
            cnt_x += 1
            if cnt_y == 1 and cnt_x == 1:
                for dy in range(n):
                    for dx in range(n):
                        N_list[a+y + dy][b+x + dx] = ' '
            else:
                go(n // 3, y*n, x*n)
    return

N = 27

N_list = [['*' for i in range(N)] for i in range(N)]

go(N // 3, 0, 0)

for i in N_list:
    print(*i)
