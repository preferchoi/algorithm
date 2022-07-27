'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

'''

for test in range(int(input())):
    N = int(input())
    N_list = list(map(int, input().split(" ")))

    print(f'#{test+1}', max(N_list) - min(N_list))
