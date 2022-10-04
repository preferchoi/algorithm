def go(n, x, y):
    if n == 1:
        return

    cnt = 0
    for dy in range(y, y + n, n // 3):
        for dx in range(x, x + n, n // 3):
            if cnt == 4:
                for hole_y in range(dy, dy + n // 3):
                    for hole_x in range(dx, dx + n // 3):
                        base_lst[hole_y][hole_x] = ' '
            else:
                go(n // 3, dx, dy)
            cnt += 1


N = int(input())
base_lst = [['*' for _ in range(N)] for _ in range(N)]
go(N, 0, 0)
for i in base_lst:
    for j in i:
        print(j, end='')
    print()
