def go(n):
    global V
    mst = [False for _ in range(V + 1)]
    key = [10 * (V + 1) for _ in range(V + 1)]
    key[0] = 0
    for _ in range(V):
        u = 0
        minV = 10 * (V + 1)
        for i in range(V + 1):
            if mst[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        mst[u] = 1
        for v in range(V + 1):
            if mst[v] == 0 and tree[u][v] > 0:
                key[v] = min(key[v], tree[u][v])
    return sum(key)


for tc in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    tree = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for i in range(E):
        a, b, c = map(int, input().split())
        tree[a][b] = c
        tree[b][a] = c

    print(f'#{tc} {go(0)}')
