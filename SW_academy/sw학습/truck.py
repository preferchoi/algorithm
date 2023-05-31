'''
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

'''
for test in range(int(input())):
    NM = list(map(int, input().split(" ")))
    N = NM[0] # 화물수
    M = NM[1] # 트럭수
    N_w = list(map(int, input().split(" "))) # 화물무게
    M_w = list(map(int, input().split(" "))) # 트럭무게
    N_w.sort()
    M_w.sort()
    N_w.reverse()
    M_w.reverse()
    x, ans = 0, 0
    # print(N_w, M_w)
    for i in M_w:
        for j in range(x, len(N_w)):
            # print(x)
            if N_w[j] <= i:
                x += 1
                ans += N_w[j]
                break
            else:
                x += 1
    print(f'#{test+1}', ans)
