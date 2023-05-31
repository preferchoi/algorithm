def go(N, mapp):

    mapp_90 = [[0]*N for _ in range(N)]

    # 90도 돌림
    for i in range(N):
        for j in range(N):
            mapp_90[i][j] = mapp[j][i]
    # print(mapp_90)
    for k in range(N, -1, -1):  # 회문 길이
        for i in range(N):  # x축
            for j in range(N - k + 1):  # y축
                q = mapp[i][j: j + k]
                t = q[::-1]

                if q == t:
                    return k

                q = mapp_90[i][j: j + k]
                t = q[::-1]

                if q == t:
                    # print(q, q[::-1])
                    return k

    return None


for tc in range(10):
    print(f'#{input()}', end=' ')
    mapp = []
    for i in range(100):
        mapp.append(list(input()))
    # print(mapp)
    N = len(mapp)

    print(go(N, mapp))
