def go(x, y, n):
    flag = False
    key = lst[y][x]
    for dy in range(y, y + n):
        for dx in range(x, x + n):
            if key != lst[dy][dx]:
                flag = not flag
                break
        if flag:
            break
    else:
        print(key, end='')
    if flag:
        print('(', end='')
        for dy in range(y, y + n, n // 2):
            for dx in range(x, x + n, n // 2):
                go(dx, dy, n // 2)
        print(')', end='')


N = int(input())
lst = [list(map(int, list(input()))) for _ in range(N)]
go(0, 0, N)
