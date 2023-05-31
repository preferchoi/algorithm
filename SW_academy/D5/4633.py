def go_2(lst):
    cnt = 1
    ans = 0
    for i in lst[::-1]:
        ans += i * cnt
        cnt *= 2
    return ans


def go_3(lst):
    cnt = 1
    ans = 0
    for i in lst[::-1]:
        ans += i * cnt
        cnt *= 3
    return ans


for tc in range(1, 1 + int(input())):
    N = list(map(int, input()))
    M = list(map(int, input()))

    tmp = []
    tmp_2 = []
    tmp_3 = []

    for i in range(len(N)):
        if N[i]:
            tmp = N[:]
            tmp[i] = 0
        else:
            tmp = N[:]
            tmp[i] = 1
        tmp_2.append(go_2(tmp))

    for i in range(len(M)):
        if not M[i]:
            tmp = M[:]
            tmp[i] = 1
            tmp_3.append(go_3(tmp))
            tmp[i] = 2
            tmp_3.append((go_3(tmp)))
        elif M[i] == 1:
            tmp = M[:]
            tmp[i] = 0
            tmp_3.append(go_3(tmp))
            tmp[i] = 2
            tmp_3.append((go_3(tmp)))
        elif M[i] == 2:
            tmp = M[:]
            tmp[i] = 0
            tmp_3.append(go_3(tmp))
            tmp[i] = 1
            tmp_3.append((go_3(tmp)))

    for i in tmp_2:
        if i in tmp_3:
            print(f'#{tc} {i}')
            break
