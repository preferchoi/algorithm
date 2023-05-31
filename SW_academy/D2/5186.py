for tc in range(1, 1 + int(input())):
    N = float(input())
    ans = ''
    cnt = -1
    flag = True
    while cnt > -13:
        if N >= 2**cnt:
            ans += '1'
            N -= 2 ** cnt
        else:
            ans += '0'
        cnt -= 1
        if N == 0:
            break
    else:
        flag = False

    print(f'#{tc}', end=' ')
    if flag:
        print(ans)
    else:
        print('overflow')