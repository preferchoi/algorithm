for tc in range(1, int(input())+1):
    ND = list(map(int, input().split()))
    N, D = ND[0], ND[1]
    cover = 2 * D + 1
    if N%cover == 0:
        ans = N//cover
    else:
        ans = N//cover + 1

    print(f'#{tc} {ans}')