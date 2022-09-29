def slice2(lst):
    if len(lst) <= 1:
        return lst
    long = len(lst)
    key = lst[long // 2]
    left, mid, right = [], [], []
    for i in lst:
        if key > i:
            left.append(i)
        elif key < i:
            right.append(i)
        else:
            mid.append(i)

    return slice2(left) + mid + slice2(right)


def slice(lst, flag):
    if not lst:
        return

    ans.append(lst[(len(lst) - 1) // 2])

    if flag:
        flag = False
        slice(lst[:(len(lst) - 1) // 2], flag)

    else:
        flag = True
        slice(lst[(len(lst) - 1) // 2 + 1:], flag)


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = slice2(A)
    ans = [A[(len(A) - 1) // 2]]
    slice(A[(len(A) - 1) // 2 + 1:], True)
    slice(A[:(len(A) - 1) // 2], False)
    cnt = 0

    for i in B:
        if i in ans:
            cnt += 1
    print(f'#{tc} {cnt}')
