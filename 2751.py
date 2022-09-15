def slice(n):
    if not n:
        return
    mid = n[len(n) // 2]
    small, big, eq = [], [], []
    for i in n:
        if mid > i:
            small.append(i)
        elif mid < i:
            big.append(i)
        else:
            eq.append(i)

    if small:
        small = slice(small)
    if big:
        big = slice(big)

    return small + eq + big


def qqq(lst):
    if not lst:
        return
    flag = True


n = int(input())
lst = [int(input()) for i in range(n)]

ans = slice(lst)

for i in ans:
    print(i)
