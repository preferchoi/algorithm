def go(sumV, idx, visited):
    global minV

    if sumV >= minV:
        return
    if sum(visited) == 1:
        sumV += N_list[idx][1]
        if sumV < minV:
            minV = sumV
        return

    for i in range(N):
        if N_list[idx][i] and visited[i]:
            tmp = visited[:]
            tmp[idx] = False
            go(sumV + N_list[idx][i], i, tmp)


for tc in range(1, 1 + int(input())):
    N = int(input()) + 2
    N_list = list(map(int, input().split()))
    tmp = []
    for i in range(0, N * 2, 2):
        tmp.append([N_list[i], N_list[i + 1]])

    q = 0
    N_list = [[] for _ in range(N)]
    for x, y in tmp:
        for dx, dy in tmp:
            N_list[q].append(abs(dx - x) + abs(dy - y))
        q += 1
    minV = 99999999
    go(0, 0, [False, False] + ([True] * (N - 2)))
    print(f'#{tc} {minV}')
