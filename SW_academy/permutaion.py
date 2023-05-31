def go(sumV, idx, visited):
    global minV

    if sumV >= minV:
        return

    if sum(visited) == 1:
        sumV += N_list[idx][0]
        if sumV < minV:
            minV = sumV
        return

    for i in range(N):
        if N_list[idx][i] and visited[i]:
            tmp = visited[:]
            tmp[idx] = False
            go(sumV + N_list[idx][i], i, tmp)


for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    minV = 9999999
    go(0, 0, [False] + ([True] * (N - 1)))
    print(f'#{tc} {minV}')
