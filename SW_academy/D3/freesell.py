'''
3
100 1 50
1000 81 83
10 10 100
'''

for test in range(1, 1+int(input())):
    NPdPg = list(map(int, input().split(" ")))
    N, Pd, Pg = NPdPg[0], NPdPg[1], NPdPg[2]
    check = 0
    # print(f'N = {N}, Pd = {Pd}, Pg = {Pg}')

    if (Pg == 100 or Pg == 0) and Pd != Pg:
        check = -1
    # 100인건 걸렀으니까 99~1까지의 수
    else:
        check = -1
        if N >= 100:
            check = 0
        else:
            for j in range(1, N + 1):
                if j * Pd % 100 == 0:
                    check = 0
                    break

    if check == 0:
        print(f'#{test} Possible')
    else:
        print(f'#{test} Broken')