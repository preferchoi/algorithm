for tc in range(1, 1 + int(input())):
    N = int(input())
    s = input()

    cnt = 0
    maxV = 0
    for i in s:
        if i == '1':
            cnt += 1
        if i == '0':
            if maxV < cnt:
                maxV = cnt
            cnt = 0
    else:
        if maxV < cnt:
            maxV = cnt

    print(f'#{tc} {maxV}')