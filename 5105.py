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
    N_list = [list(input()) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    flag = 0
    for y in range(N):
        for x in range(N):
            if N_list[y][x] == '2':
                flag = 1
                break
        if flag:
            break

    queue = [[y, x]]
    visited[y][x] = 1
    go = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    print(f'#{tc}', end=' ')
    while queue:
        dy, dx = queue.pop()
        for a, b in go:
            if_y, if_x = dy + a, dx + b
            if 0 <= if_y < N and 0 <= if_x < N:
                if N_list[if_y][if_x] == '0' and visited[if_y][if_x] == 0:
                    queue.append([if_y, if_x])
                    visited[if_y][if_x] = visited[dy][dx] + 1
                if N_list[if_y][if_x] == '3':
                    visited[if_y][if_x] = visited[dy][dx] + 1
                    flag = 0
                    break
        if not flag:
            print(visited[if_y][if_x]-2)
            break
    else:
        print(0)