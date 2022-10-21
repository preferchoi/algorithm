for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    mapp = []
    for i in range(N):
        mapp.append(list(map(int, input().split())))
    # print(mapp)
    key = [0]
    key += [1] * M
    key += [0]
    #print(key)
    # N - K + 1 만큼이면 범위값
    # 5 - 3 = 2     range(3) = 0, 1, 2
    count = 0
    for i in range(N):
        for j in range(N - M + 1):
            if j == 0:
                if mapp[i][j:j + M + 1] == key[1:M + 2]:
                    count += 1
                    #print(mapp[i][j:j + M + 1], key[1:M + 2])
            elif j == N - M:
                if mapp[i][j - 1:j + M] == key[:M + 1]:
                    count += 1
                    #print(mapp[i][j - 1:j + M], key[:M + 1])
            else:
                if mapp[i][j - 1:j + M + 1] == key:
                    #print(mapp[i][j - 1:j + M + 1], key)
                    count += 1

    spin_mapp = []
    for i in range(N):
        Q = []
        for j in range(N):
            Q.append(mapp[j][i])
        spin_mapp.append(Q)
    #print(spin_mapp)

    for i in range(N):
        for j in range(N - M + 1):
            if j == 0:
                if spin_mapp[i][j:j + M + 1] == key[1:M + 2]:
                    count += 1
                    #print(spin_mapp[i][j:j + M + 1], key[1:M + 2])
            elif j == N - M:
                if spin_mapp[i][j - 1:j + M] == key[:M + 1]:
                    count += 1
                    #print(spin_mapp[i][j - 1:j + M], key[:M + 1])
            else:
                if spin_mapp[i][j - 1:j + M + 1] == key:
                    count += 1
                    #print(spin_mapp[i][j - 1:j + M + 1], key)
    print(f'#{tc} {count}')