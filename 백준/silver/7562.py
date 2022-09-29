delta = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
for tc in range(1, 1 + int(input())):
    N = int(input())
    now_x, now_y = map(int, input().split())
    goal_x, gaol_y = map(int, input().split())

    lst = [[True for _ in range(N)] for _ in range(N)]
    q = [[now_y, now_x, 0]]
    flag = False
    while q:
        y, x, d = q.pop(0)
        if gaol_y == y and goal_x == x:
            break
        d += 1

        for dy, dx in delta:
            ify, ifx = y + dy, x + dx

            if 0 <= ify < N and 0 <= ifx < N and lst[ify][ifx]:
                q.append([ify, ifx, d])
                lst[ify][ifx] = False

        if flag:
            break
    print(d)
