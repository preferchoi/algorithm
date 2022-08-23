'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

'''
for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    start_y, start_x = 0, 0
    flag = 0
    for y in range(N):
        for x in range(N):
            if N_list[y][x] == 2:
                start_y, start_x = y, x
                flag = 1
                break
        if flag:
            break

    print(f'#{tc}', end=' ')
    dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
    stack = [[start_y, start_x]]
    while stack:
        y, x = stack.pop()
        for i in range(4):
            go_y, go_x = y + dy[i], x + dx[i]

            if 0 <= go_y < N and 0 <= go_x < N:
                if N_list[go_y][go_x] == 0:
                    N_list[go_y][go_x] = 1
                    stack.append([go_y, go_x])
                if N_list[go_y][go_x] == 3:
                    flag = 0
                    print(1)
                    break
        if not flag:
            break
    else:
        print(0)
