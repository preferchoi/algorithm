for tc in range(1, 1 + int(input())):
    N, Q = map(int, input().split())
    N_list = [0 for _ in range(N)]
    for i in range(1, 1 + Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            N_list[j] = i
    print(f'#{tc}', end=' ')
    print(*N_list)


