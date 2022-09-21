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
        print('end2')
        return

    '''
    리스트 조작할 코드 위치
    '''
    # 리스트 안에서 가장 큰 값
    max_num = max(lst[n:])
    # 큰 값이 몇 개 있는지 셈, 이미 정렬된 부분은 냅둠
    max_count = lst[n:].count(max_num)
    # value,index 쌍으로 넣어서 나중에 정렬
    tmp_idx = []
    tmp_V = []
    cnt = 0
    while n + cnt < N:
        tmp = 0
        # 리스트 안의 max값 중에서 맨 뒤에 있는 idx
        r_max_index = lst[::-1].index(max_num)
        max_index = len(lst) - 1 - r_max_index
        # 교체
        if lst[max_index] != lst[n]:
            lst[max_index], lst[n] = lst[n], lst[max_index]
            tmp_V.append(lst[max_index])
            tmp_idx.append(max_index)
        else:
            tmp = 0
            while lst[n + tmp] == lst[max_index]:
                tmp += 1
                if lst[max_index] != lst[n + tmp]:
                    lst[max_index], lst[n] = lst[n], lst[max_index]
                    tmp_V.append(lst[max_index])
                    tmp_idx.append(max_index)
        print('swap', lst[max_index], lst[n + tmp], n + tmp, max_index)
        cnt += 1
        if cnt >= max_count:
            print('tmp_V', tmp_V, 'tmp_idx', tmp_idx)
            break
    else:
        print('tmp_V', tmp_V, 'tmp_idx', tmp_idx)
        print('end1', *lst)
        return
        # 재귀 부분
    go(n + cnt)


for tc in range(1, 1 + int(input())):
    lst, N = input().split()
    lst, N = list(map(int, lst)), int(N)
    print(f'#{tc} {lst}, {N}')
    # 교환 횟수가 충분할 때
    # 왜 N 보다 같을 때 교환 횟수가 충분?
    # 선택 정렬을 이용, 앞부터 큰 순으로 인덱스 교체, 항상 최대 크기를 유지
    if N >= len(lst):
        lst.sort()
        lst.reverse()
        if N - len(lst) % 2:
            lst[-1], lst[-2] = lst[-2], lst[-1]
    # 교환 횟수가 전부 돌기엔 모자랄 때
    else:
        go(0)

    print(f'#{tc}', ''.join(map(str, lst)))

'''
13524
53124
54123
54321

13524
15324
51324
54321

12453
52413
54213
54312
54321

12453
32451
34251
34521
54321



'''
