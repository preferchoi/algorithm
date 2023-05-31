'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

'''
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for tc in range(1, 1 + int(input())):
    Y, X, K = map(int, input().split())
    lst = [[0 for _ in range(X)] for _ in range(Y)]

    for _ in range(K):
        inp_y, inp_x = map(int, input().split())
        lst[inp_y][inp_x] = 1

    ans = 0
    for y in range(Y):
        for x in range(X):
            if lst[y][x] == 1:
                lst[y][x] = 0
                ans += 1
                q = [[y, x]]
                while q:
                    q_y, q_x = q.pop(0)
                    for dy, dx in delta:
                        ify, ifx = q_y + dy, q_x + dx
                        if 0 <= ifx < X and 0 <= ify < Y and lst[ify][ifx]:
                            q.append([ify, ifx])
                            lst[ify][ifx] = 0
    print(ans)
