'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2

'''
'''
@초 지난 뒤 붕어빵 수
M * (@//K)
'''
for t in range(int(input())):
    N, M, K = map(int, input().split(" "))
    time_lap = list(map(int, input().split(" ")))
    time_lap.sort()
    # print(N, M, K)
    # print(time_lap)

    sup = list(range(M, time_lap[-1] + 1, M))
    # print(sup)
    count_make = 0
    if M > time_lap[0]:
        print(f'#{t+1} Impossible')
    else:
        for i in range(1, time_lap[-1]+1):
            if i in sup:    # 시간지나면 붕어빵 만듬
                count_make += K
            if i in time_lap:
                count_make -= 1
            if count_make < 0:
                print(f'#{t + 1} Impossible')
                break
            if i == time_lap[-1]:
                print(f'#{t+1} Possible')
    print(count_make)