T = int(input())

for test in range(1, T+1):
    num = int(input())
    N_list = input().split()
    N_list.sort()
    # print(N_list)

    count = 0
    max = 0
    for i in range(len(N_list)-2):
        if N_list[i] != N_list[i+1]:
            if max <= count:
                max = count
                max_num = N_list[i]
            count = 0
        count += 1
    print(f'#{num}', max_num)

# for t in range(int(input())):
#     n, d = input(), input().split()
#     print(f'#{n} {max(set(d),key=d.count)}')