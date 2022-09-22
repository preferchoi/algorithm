'''
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10

'''


def go(n):
    # 교환 횟수 전부 소모
    if n >= N:
        return
    #
    if lst == idea:
        if len(lst) != len(set(lst)):
            pass
        elif N - len(lst) % 2:
            lst[-1], lst[-2] = lst[-2], lst[-1]
        return

    '''
    리스트 조작할 코드 위치
    '''
    # 리스트 안에서 가장 큰 값
    max_num = max(lst[n:])
    # 큰 값이 몇 개 있는지 셈, 이미 정렬된 부분은 냅둠
    max_count = lst[n:].count(max_num)
    tmp_idx = []
    # 가장 큰 값의 위치
    for i in range(len(lst[n:])):
        if lst[i] == max_num:
            tmp_idx.append(n + i)
    tmp_idx.sort(reverse=True)
    print(tmp_idx)
    tmp_v = []
    cnt = 0
    tmp = 0
    while n + cnt < N and cnt < max_count:
        print(n + cnt + tmp, lst[n + tmp])
        while True:
            if lst[tmp_idx[cnt]] >= lst[n + tmp]:
                print(n + tmp, tmp_idx[cnt], lst[n + tmp], lst[tmp_idx[cnt]])
                tmp += 1
            else:
                break
        print(n + cnt + tmp, lst[n + tmp])
        break
        cnt += 1

    else:
        for i in tmp_idx:
            tmp_v.append(lst[i])
        print(tmp_v)
        tmp_v.sort()
        for i in range(len(tmp_idx)):
            lst[tmp_idx[i]] = tmp_v[i]
        if n + cnt >= N:
            return
        else:
            n += cnt

            # 재귀 부분
    go(n + 1)


for tc in range(1, 1 + int(input())):
    lst, N = input().split()
    lst, N = list(map(int, lst)), int(N)
    idea = sorted(lst, reverse=True)
    print(f'#{tc} {lst}, {N}')

    go(0)

    print(f'#{tc}', ''.join(map(str, lst)))

'''
42237788
82237784
88237724 -> 88237742
88737242
88773242


2
88220388 5
88220388 2

'''
