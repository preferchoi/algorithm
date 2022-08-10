'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

'''
TC = int(input())
for tc in range(1, 1 + TC):
    K, N, M = map(int, input().split())
    # 한번에 갈 수 있는 K 종점인 N 충전 가능한 정류장 수 M
    M_list = list(map(int, input().split()))

    bus_im_here = 0
    cnt = 0

    while cnt < M + 1:
        cnt += 1
        for charge in range(K, 0, -1):
            if bus_im_here + charge in M_list:
                bus_im_here += charge
                # print(bus_im_here)
                break

        if bus_im_here + K >= N:
            break

    if cnt > M:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {cnt}')
