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
    queue = []
    result = 0
    deep = -1

    y = -1
    for i in N_list:
        y += 1
        x = -1
        for j in i:
            x += 1
            if j == 2:
                queue.append([y, x, deep])
                break
        if queue:
            break

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0

    while not result:
        if not queue:
            deep = 0
            break
        y, x, deep = queue.pop(0)
        deep += 1

        for i in range(4):
            ify = y + dy[i]
            ifx = x + dx[i]

            if 0 <= ifx < N and 0 <= ify < N and not visited[ify][ifx]:
                if N_list[ify][ifx] == 0:
                    visited[ify][ifx] = True
                    queue.append([ify, ifx, deep])
                if N_list[ify][ifx] == 3:
                    result = 1

    print(f'#{tc} {deep}')

