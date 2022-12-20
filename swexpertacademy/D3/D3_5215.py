from itertools import combinations
'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400

'''
for tc in range(1, 1 + int(input())):
    N, Limit = map(int, input().split())

    set_list = []
    for i in range(N):
        taste, cal = map(int, input().split())
        set_list.append([taste, cal])

    if_list = []

    for i in range(1, N+1):
        a = list(combinations(set_list, i))
        for j in a:
            total_t = 0
            total_c = 0
            for k in j:
                total_t += k[0]
                total_c += k[1]
                if total_c >Limit:
                    break
            if total_c <= Limit:
                if_list.append(total_t)
    print(f'#{tc} {max(if_list)}')