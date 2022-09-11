def slice(lst):
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

    return slice(left) + mid + slice(right)


for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = list(map(int, input().split()))

    print(f'#{tc}', slice(N_list)[N // 2])
