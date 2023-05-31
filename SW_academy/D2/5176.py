'''
3
6
8
15

'''


def inorder_traverse(T):
    global cnt

    if N_list[T][0]:
        inorder_traverse(N_list[T][0])

    N_list[T][2] = cnt
    cnt += 1
    if N_list[T][1]:
        inorder_traverse(N_list[T][1])



for tc in range(1, 1 + int(input())):
    N = int(input())

    N_list = [[0, 0, 0] for i in range(N + 1)]
    # print(N_list)
    cnt = 1
    num = 2

    while num <= N:
        if not N_list[cnt][0]:
            N_list[cnt][0] = num
            num += 1
        if num > N:
            break
        if not N_list[cnt][1]:
            N_list[cnt][1] = num
            num += 1
            cnt += 1

    cnt = 1
    inorder_traverse(cnt)
    # print(N_list)
    print(f'#{tc} {N_list[1][2]} {N_list[N // 2][2]}')
