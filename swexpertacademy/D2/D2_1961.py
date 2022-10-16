for tc in range(1, 1 + int(input())):
    N = int(input())
    mapp = []
    for i in range(N):
        mapp.append(input().split())
    # print(mapp)

    v1_list = []
    for i in range(N - 1, -1, -1):
        q = []
        for j in range(N):
            q.append(mapp[j][i])
        v1_list.append(q)
    # print(v1_list)

    v2_list = []
    for i in range(N - 1, -1, -1):
        q = []
        for j in range(N - 1, -1, -1):
            q.append(mapp[i][j])
        v2_list.append(q)
    # print(v2_list)

    v3_list = []
    for i in range(N):
        q = []
        for j in range(N - 1, -1, -1):
            q.append(mapp[j][i])
        v3_list.append(q)
    # print(v3_list)

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(v3_list[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(v2_list[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(v1_list[i][j], end='')
        print()
