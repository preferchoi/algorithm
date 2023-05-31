'''
3
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1

'''
for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = list(map(int, input().split()))

    cnt = 0
    pre = 0
    maxV = 0
    for i in N_list:
        cnt += 1
        if pre <= i:
            if maxV < cnt:
                maxV = cnt
        else:
            cnt = 1
        pre = i
    print(f'#{tc} {maxV}')
