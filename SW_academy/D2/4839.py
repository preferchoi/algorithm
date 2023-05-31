'''
3
400 300 350
1000 299 578
1000 222 888

'''
def find(P_start, P_end, N, count):
    P_mid = (P_start + P_end) // 2
    count += 1

    if P_mid == N:
        return count
    elif P_mid < N:
        count = find(P_mid, P_end, N, count)
    elif P_mid > N:
        count = find(P_start, P_mid, N, count)

    return count


TC = int(input())
for tc in range(1, 1 + TC):
    P, A, B = map(int, input().split())

    count_A = find(1, P, A, 0)
    count_B = find(1, P, B, 0)

    if count_A > count_B:
        print(f'#{tc} B')
    elif count_A < count_B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

#
# def slice(P_list, Q, deep):
#     deep += 1
#     mid = round(len(P_list) / 2)
#     R_list, L_list = P_list[:mid], P_list[mid:]
#
#     if Q == P_list[mid]:
#         return deep
#
#     elif Q in R_list:
#         return slice(R_list, Q, deep)
#
#     elif Q in L_list:
#         return slice(L_list, Q, deep)
#
#
# for tc in range(1, 1 + int(input())):
#     P, A, B = map(int, input().split())
#     P_list = list(range(P))
#     P_list[A], P_list[B] = 'A', 'B'
#     # print(P_list, P_list[A], P_list[B])
#
#     ans_A = slice(P_list, 'A', 0)
#     ans_B = slice(P_list, 'B', 0)
#
#     print(f'#{tc}', end=' ')
#     if ans_A - ans_B < 0:
#         print('A')
#     elif ans_A - ans_B > 0:
#         print('B')
#     else:
#         print(0)
