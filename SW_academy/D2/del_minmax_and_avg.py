'''
10
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
345 37 2375 23 32 132 47 76 26 12
765 26 346 16 263 36 61 569 35 70
912 923 7456 879 8237 864 1170 6893 34 9
934 73 456 3 47 32 74 18 23 345
72 812 73 384 23 76 54 94 556 834
87 51 438 126 48 13 834 162 805 21
213 21 45 87 476 59 98 325 900 11
'''
T = int(input())
for test in range(1, T+1):

    N_list = input().split(" ")

    for i in range(len(N_list)):
        N_list[i] = int(N_list[i])

    N_list.sort()
    N_list.remove(N_list[len(N_list)-1])
    N_list.remove(N_list[0])

    avg = sum(N_list)/len(N_list)
    print(f'#{test}', round(avg))