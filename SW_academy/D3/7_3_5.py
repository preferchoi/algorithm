'''
2
1 2 3 4 5 6 7
5 24 99 76 1 77 6
'''

for test in range(1, int(input())+1):
    num_list = list(map(int, input().split(" ")))
    num_list.sort()
    num_list.reverse()

    sum_list = []
    for i in num_list:
        for j in num_list:
            for k in num_list:
                if not i == j and not i == k and not j == k:
                    sum_list.append(i + j + k)
    sum_list = list(set(sum_list))
    sum_list.sort()
    sum_list.reverse()
    print(f'#{test}', sum_list[4])