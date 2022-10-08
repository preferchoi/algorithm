delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for tc in range(int(input())):
    X, Y = map(int, input().split())
    lst = [list(input()) for _ in range(Y)]

    sang = []
    fire = []
    for i in range(Y):
        for j in range(X):
            if lst[i][j] == '@':
                sang = [i, j]
                lst[i][j] = 0
            if lst[i][j] == '*':
                fire.append([i, j])

    q = [sang + [1]]
    while q:
        y, x, d = q.pop(0)
        for dy, dx in delta:
            ify, ifx = y + dy, x + dx
            if 0 <= ifx < X and 0 <= ify < Y:
                if lst[ify][ifx] == '.':
                    lst[ify][ifx] = d
                    q.append([ify, ifx, d + 1])

    # 갈 수 없는 길은 벽으로
    for i in range(Y):
        for j in range(X):
            if lst[i][j] == '.':
                lst[i][j] = '#'

    for a in fire:
        q = [a + [1]]
        while q:
            y, x, d = q.pop(0)
            for dy, dx in delta:
                ify, ifx = y + dy, x + dx
                if 0 <= ifx < X and 0 <= ify < Y:
                    if lst[ify][ifx] != '#' and lst[ify][ifx] != '@' and lst[ify][ifx] != '*':
                        if lst[ify][ifx] >= d:
                            lst[ify][ifx] = '*'
                            q.append([ify, ifx, d + 1])

    # 탈출 가능한 경로들
    ans = []
    # 외곽 돌면서 숫자인 것 잧음
    for y in [0, Y - 1]:
        for x in range(X):
            if lst[y][x] != '#' and lst[y][x] != '*':
                ans.append(lst[y][x])
    for y in range(Y):
        for x in [0, X - 1]:
            if lst[y][x] != '#' and lst[y][x] != '*':
                ans.append(lst[y][x])
    
    # 외곽에 숫자 있으면 최소값 출력
    if ans:
        print(min(ans) + 1)
    else:
        print('IMPOSSIBLE')
