'''
0 1 0 0 0 1 0 0 1 0
0 1 0 0 0 1 1 1 1 0
0 1 0 0 0 1 0 0 1 0
0 1 1 1 1 1 0 0 1 0
0 1 0 0 0 1 0 0 1 0
0 1 0 0 0 1 1 1 1 0
0 1 0 0 0 1 0 0 1 0
0 1 1 1 1 1 0 0 1 0
0 1 0 0 0 1 0 0 1 0
0 1 0 0 0 2 0 0 1 0

'''
for tc in range(1, 11):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(100)]
    N = len(N_list)

    line_list = []
    cnt = -1
    start = 0

    for i in N_list[-1]:
        cnt += 1
        if i == 1:
            line_list.append(cnt)
        if i == 2:
            line_list.append(cnt)
            start = cnt

    start = line_list.index(start)

    for i in range(99, -1, -1):
        l_x, r_x = line_list[start] - 1, line_list[start] + 1

        if r_x < N and N_list[i][r_x] == 1:
            start += 1
            continue

        if l_x >= 0 and N_list[i][l_x] == 1:
            start -= 1
            continue

    print(f'#{tc} {line_list[start]}')
