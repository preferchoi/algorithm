for tc in range(10):
    print(f'#{input()}', end=' ')
    mapp = []
    for i in range(100):
        mapp.append(list(input()))
    # print(mapp)
    bot = True
    N = len(mapp)
    for key in range(100, -1, -1):
        for x in range(N):
            for y in range(N - key + 1):
                bot = True
                for i in range(key):
                    # print(key, x, y, i, -(100 - key + 1 + i))
                    if mapp[x][y + i - 1] != mapp[x][y + -(100 - key + 1 + i)]:
                        bot = False
                        break
                    if not bot:
                        break
                if bot:
                    break
                vot = True
                for i in range(key):
                    if mapp[y + i - 1][x] != mapp[y - (100 - key + 1 + i)][x]:
                        bot = False
                    if not bot:
                        break
                if bot:
                    break
            if bot:
                break
        if bot:
            print(key)
            break
