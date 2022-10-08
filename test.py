def ispattern(y, x, c):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for d in range(4):
        if c == '.':
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
                continue
            if arr[ny][nx] == '.':
                return True
            if arr[ny][nx] == '?':
                arr[ny][nx] = '#'
        elif c == '#':
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
                continue
            if arr[ny][nx] == '#':
                return True
            if arr[ny][nx] == '?':
                arr[ny][nx] = '.'


T = int(input())
for testcase in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    flag = 0
    print(f'#{testcase} ', end='')
    for i in range(N):
        for j in range(M):
            if ispattern(i, j, arr[i][j]):
                flag = 1
                break
        if flag == 1:
            print('Impossible')
            break
    else:
        print('Possible')