'''
10
5 16
3 1 3 5 6
2 10
7 7
3 120
83 64 36
4 416
299 239 116 128
5 1535
351 228 300 623 954
10 2780
268 61 201 535 464 168 491 275 578 153
10 1162
73 857 502 826 923 653 168 396 353 874
15 8855
3711 576 9081 3280 1413 6818 5142 2981 1266 484 5757 2451 6961 4862 2086
15 57209
8903 5737 3749 8960 724 6295 1240 4325 8023 3640 2223 639 4161 5330 4260
20 78988
3811 2307 3935 5052 4936 3473 6432 7032 1560 1992 5332 7000 4020 9344 2732 8815 9924 8998 9540 4640

'''

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    minV = sum(N_list)

    for i in range(1 << N):
        tmp = 0
        for j in range(N):
            if i & (1 << j):
                tmp += N_list[j]
            if tmp > minV:
                break
        if M <= tmp < minV:
            minV = tmp

    print(f'#{tc} {minV - M}')
