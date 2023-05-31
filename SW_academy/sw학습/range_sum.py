'''
2
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821

'''

for test in range(int(input())):
    NM = list(map(int, input().split(" ")))
    N, M = NM[0], NM[1]
    num_list = list(map(int, input().split()))

    num_max, num_min = 0, 99999

    for i in range(N-M+1):
        num_set = sum(num_list[i:i+M])
        if num_max <= num_set:
            num_max = num_set
        if num_min >= num_set:
            num_min = num_set
    print(f'#{test+1}', num_max-num_min)