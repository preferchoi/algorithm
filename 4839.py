'''
3
400 300 350
1000 299 578
1000 222 888

'''


def slice(P_list, Q, deep):
    deep += 1
    mid = round(len(P_list) / 2)
    R_list, L_list = P_list[:mid], P_list[mid:]

    if Q == P_list[mid]:
        return deep

    elif Q in R_list:
        return slice(R_list, Q, deep)

    elif Q in L_list:
        return slice(L_list, Q, deep)


for tc in range(1, 1 + int(input())):
    P, A, B = map(int, input().split())
    P_list = list(range(P))
    P_list[A], P_list[B] = 'A', 'B'
    # print(P_list, P_list[A], P_list[B])

    ans_A = slice(P_list, 'A', 0)
    ans_B = slice(P_list, 'B', 0)

    print(f'#{tc}', end=' ')
    if ans_A - ans_B < 0:
        print('A')
    elif ans_A - ans_B > 0:
        print('B')
    else:
        print(0)
