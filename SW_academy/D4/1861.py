for tc in range(1, 1 + int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    go = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    maxV, max_num = 0, 0
    num = 0
    visit = [True for _ in range(N * N + 1)]
    while num + maxV < N * N - 1:
        num += 1
        if visit[num]:
            flag = False

            for y in range(N):
                for x in range(N):
                    if lst[y][x] == num:
                        flag = True
                        break
                if flag:
                    break
            q = [[y, x]]

            cnt = num
            while q:
                y, x = q.pop(0)
                for dy, dx in go:
                    if_y, if_x = y + dy, x + dx
                    if 0 <= if_y < N and 0 <= if_x < N:
                        if lst[if_y][if_x] == cnt + 1:
                            cnt += 1
                            visit[cnt] = False
                            q.append([if_y, if_x])
                            break
            else:
                if maxV < cnt - num + 1:
                    maxV = cnt - num + 1
                    max_num = num
    print(f'#{tc} {max_num} {maxV}')
