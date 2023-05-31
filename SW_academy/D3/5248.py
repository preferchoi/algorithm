def go(n):
    for i in tree[n]:
        if visited[i]:
            visited[i] = False
            go(i)

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(N + 1)]
    visited = [True for _ in range(N + 1)]
    visited[0] = False
    for i in range(0, M * 2, 2):
        tree[lst[i]] += [lst[i + 1]]
        tree[lst[i + 1]] += [lst[i]]

    cnt = 0

    for i in range(len(tree)):

        if visited[i]:
            visited[i] = False
            cnt += 1
            go(i)
    print(f'#{tc} {cnt}')
