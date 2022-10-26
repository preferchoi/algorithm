for tc in range(1, 1+ int(input())):
    N, M = map(int, input().split())
    mapp = []
    for i in range(N):
        mapp.append(list(map(int, input().split())))

    maxi = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            q = 0
            for k in range(M):
                q += sum(mapp[i+k][j:j+M])
            if q > maxi:
                maxi = q
    print(f'#{tc} {maxi}')