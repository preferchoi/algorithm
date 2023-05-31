'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

'''
TC = int(input())
for tc in range(1, 1 + TC):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    # print(N_list)
    minV = sum(N_list)
    maxV = - sum(N_list)
    for i in range(N-M + 1):
        sumV = 0
        for j in range(i, i+M):
            sumV += N_list[j]
        # print(sumV)
        if maxV < sumV:
            maxV = sumV
        if minV > sumV:
            minV = sumV
    print(f'#{tc} {maxV - minV}')