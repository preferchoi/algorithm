def go(deep, n, x, y):
    key = base_lst[y][x]

    flag = False
    for dy in range(y, y + n):
        for dx in range(x, x + n):
            if key != base_lst[dy][dx]:
                flag = True
                break
        if flag:
            break
    else:
        ans[key] += 1
    if flag:
        for dy in range(y, y + n, n // 3):
            for dx in range(x, x + n, n // 3):
                go(deep + 1, n // 3, dx, dy)


N = int(input())
base_lst = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]

go(0, N, 0, 0)

for i in range(-1, 2):
    print(ans[i])
