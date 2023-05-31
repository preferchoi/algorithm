'''
3
2 7
3 15
36 1007

'''

from collections import deque


def bfs(n, cnt):
    q = deque([[n, cnt]])
    visited = set()
    visited.add(n)

    while q:
        n, cnt = q.popleft()

        if n == M:
            return cnt

        tmp = 0
        if n + 1 not in visited:
            tmp = n + 1
            if tmp < 1000001:
                q.append([tmp, cnt + 1])
                visited.add(tmp)
        if n - 1 not in visited:
            tmp = n - 1
            if tmp < 1000001:
                q.append([tmp, cnt + 1])
                visited.add(tmp)
        if n - 10 not in visited:
            tmp = n - 10
            if tmp < 1000001:
                q.append([tmp, cnt + 1])
                visited.add(tmp)
        if n * 2 not in visited:
            tmp = n * 2
            if tmp < 1000001:
                q.append([tmp, cnt + 1])
                visited.add(tmp)




for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N, 0)}')
