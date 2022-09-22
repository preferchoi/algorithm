def go(x, y, sumV):
    sumV += N_list[y][x]
    if x == n - 1 and y == n - 1:
        global Min
        if Min > sumV:
            Min = sumV
    if 0 <= y < n - 1 and 0 <= x < n - 1:
        go(x, y + 1, sumV)
        go(x + 1, y, sumV)
    elif 0 <= x < n - 1:
        go(x + 1, y, sumV)
    elif 0 <= y < n - 1:
        go(x, y + 1, sumV)


for test in range(int(input())):
    n = int(input())
    N_list = [list(map(int, input().split())) for _ in range(n)]

    X = 0
    Y = 0

    Min = 9999999
    set_list = []

    go(X, Y, 0)

    print(f'#{test + 1}', Min)


