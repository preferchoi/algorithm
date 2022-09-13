def go(n):
    left, right = tree[n][1], tree[n][2]
    if left:
        go(left)
    if right:
        go(right)
    if not tree[n][0]:
        tree[n][0] = tree[left][0] + tree[right][0]


for tc in range(1, 1 + int(input())):
    N, M, L = map(int, input().split())

    tree = [[0, 0, 0] for i in range(N + 1)]
    for _ in range(M):
        node, data = map(int, input().split())
        tree[node][0] = data
    # print(N_list)
    cnt = 1
    num = 2
    while num <= N:
        if not tree[cnt][1]:
            tree[cnt][1] = num
            num += 1
        if num > N:
            break
        if not tree[cnt][2]:
            tree[cnt][2] = num
            num += 1
            cnt += 1

    go(1)
    print(f'#{tc} {tree[L][0]}')
