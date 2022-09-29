from collections import deque


def go():
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            ifx, ify = x + dx, y + dy
            if 0 <= ifx < N and 0 <= ify < N:
                tmp = lst[ify][ifx] - lst[y][x]
                if tmp < 0:
                    tmp = 0
                if visited[y][x] + 1 + tmp < visited[ify][ifx]:
                    visited[ify][ifx] = visited[y][x] + 1 + tmp
                    q.append([ifx, ify])


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, 1 + int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1000000 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    goal_x, goal_y = N - 1, N - 1
    go()
    print(f'#{tc} {visited[N - 1][N - 1]}')
