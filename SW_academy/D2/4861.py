def finding(mapp):
    mapp_rev = [[0 for _ in range(x)] for _ in range(x)]
    for i in range(x):
        for j in range(x):
            mapp_rev[i][j] = mapp[j][i]

    for i in range(len(mapp)):
        for j in range(x - y + 1):
            key = mapp[i][j:j + y]
            key.reverse()
            if mapp[i][j:j + y] == key:
                return mapp[i][j:j + y]

        for j in range(x - y + 1):
            key = mapp_rev[i][j:j + y]
            key.reverse()
            if mapp_rev[i][j:j + y] == key:
                return mapp_rev[i][j:j + y]


for tc in range(1, 1 + int(input())):
    x, y = map(int, input().split())
    mapp = []
    for _ in range(x):
        mapp.append(list(input()))

    print(f'#{tc}', end=" ")
    for i in finding(mapp):
        print(i, end="")
    print()
