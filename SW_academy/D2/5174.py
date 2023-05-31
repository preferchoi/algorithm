for tc in range(1, 1 + int(input())):
    E, N = map(int, input().split())
    N_list = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(max(N_list) + 1)]
    for i in range(0, 2 * E, 2):
        if not tree[N_list[i]][0]:
            tree[N_list[i]][0] = N_list[i + 1]
        else:
            tree[N_list[i]][1] = N_list[i + 1]

    cnt = 0
    queue = [N]
    while queue:
        s = queue.pop(0)
        cnt += 1
        if tree[s][0] != 0:
            queue.append(tree[s][0])
            tree[s][0] = 0
            if tree[s][1] != 0:
                queue.append(tree[s][1])
                tree[s][1] = 0
    print(f'#{tc} {cnt}')
