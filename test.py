def cut(Lst):
    total_cnt = 0

    for i in range(len(Lst)):
        cnt = 1
        if Lst[i] == ')':  #
            for j in range(i, -1, -1):
                if Lst[j] == '(':
                    for k in Lst[j:i + 1]:
                        if k == '0':
                            cnt += 1
                    total_cnt += cnt
                    Lst[j] = 1
                    Lst[i] = 1
                    break

    return total_cnt


for tc in range(1, int(input()) + 1):
    N = input().split('()')
    N = '0'.join(N)
    lst = list(N)

    print(f'#{tc} {cut(lst)}')

# 0 1 1 1 0 0 1 1 0 1 0 1 1 1 0 1