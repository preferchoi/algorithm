'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

'''

for test in range(int(input())):
    KNM = list(map(int, input().split(" ")))
    k, n, m = KNM[0], KNM[1], KNM[2] # k - 한번에 갈 수 있는 정거장 수 n- 종점 정거장 번호 m- 충전기가 설치된 정거장의 수
    station = list(map(int, input().split(" ")))

    way = [False]
    for i in range(1, n+1):
        if i in station:
            way.append(True)
        else:
            way.append(False)
    # print(way)

    here = 0
    count = 0
    doit = False
    for i in range(n):
        for j in range(here+k, here, -1):
            doit = False
            if j >= n:
                doit = True
                break
            if way[j]:
                here = j
                count += 1
                doit = True
                break
        if not doit:
            count = 0
            break
    print(f'#{test+1}', count)