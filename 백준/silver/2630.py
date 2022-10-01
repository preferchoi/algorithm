def go(x, y, n):
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
        for dy in range(y, y + n, n // 2):
            for dx in range(x, x + n, n // 2):
                go(dx, dy, n // 2)


N = int(input())
base_lst = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]

go(0, 0, N)
for i in ans:
    print(i)
