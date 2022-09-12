def slice(lst, flag):
    if not lst:
        return
    ans.append(lst[len(lst) // 2])

    if flag:
        flag = False
        slice(lst[len(lst) // 2 + 1:], flag)
        slice(lst[:len(lst) // 2], flag)
    else:
        flag = True
        slice(lst[:len(lst) // 2], flag)
        slice(lst[len(lst) // 2 + 1:], flag)


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans, flag = [], True
    slice(A, flag)

    cnt = 0
    for i in B:
        if i in ans:
            cnt += 1
    print(f'#{tc} {cnt}')
