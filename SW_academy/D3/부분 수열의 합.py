    from itertools import combinations
    '''
    1
    4 3
    1 2 1 2
    
    '''
    for tc in range(1, 1 + int(input())):
        N, target = map(int, input().split())
        num_list = list(map(int, input().split()))
        # print(N, target, num_list)
        num_list.sort()
        num_set = set(num_list)

        num_dict ={}
        for i in num_set:
            count = 0
            for j in num_list:
                if i == j:
                    count += 1
                num_dict[i] = count

        ans_list = []
        for i in range(1, 1 + len(num_list)):
            a = combinations(num_list, i)
            for j in a:
                if sum(j) == target:
                    ans_list.append(j)
        # print(ans_list)

        print(f'#{tc} {len(ans_list)}')
