'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

'''
TC = int(input())
for tc in range(1, 1 + TC):
    N = int(input())
    N_list = list(map(int, input().split()))
    for _ in range(N):
        for i in range(N - 1):
            if N_list[i] > N_list[i+1]:
                N_list[i], N_list[i+1] = N_list[i+1], N_list[i]

    print(f'#{tc} {N_list[-1] - N_list[0]}')