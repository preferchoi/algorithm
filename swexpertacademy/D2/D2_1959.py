for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    # print(N, N_list, M, M_list)
    t = 0
    if N < M:
        t = N
        N = M
        M = t
        t = N_list
        N_list = M_list
        M_list = t
    maxi = 0
    for i in range(N - M + 1):
        key = 0
        for j in range(M):
            key += N_list[i+j]*M_list[j]
        if maxi < key:
            maxi = key
    print(f'#{tc} {maxi}')