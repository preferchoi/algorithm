'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

'''


def order(T, pre):
    global flag
    if N_list[T][2] < N_list[pre][2]:
        N_list[T][2], N_list[pre][2] = N_list[pre][2], N_list[T][2]
        flag = False
    if N_list[T][0]:
        order(N_list[T][0], T)
    if N_list[T][1]:
        order(N_list[T][1], T)


for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [[0, 0, 0, [0, 0]] for _ in range(N + 1)]
    num = 1
    for i in list(map(int, input().split())):
        N_list[num][2] = i
        num += 1

    cnt = 1
    num = 2
    while num <= N:
        if not N_list[cnt][0]:
            N_list[cnt][0] = num
            N_list[num][3][0] = cnt
            num += 1
        if num > N:
            break
        if not N_list[cnt][1]:
            N_list[cnt][1] = num
            N_list[num][3][1] = cnt
            num += 1
            cnt += 1
    flag = True
    while flag:
        flag = True
        order(1, 0)
    stack = [N]
    ans = - N_list[N][2]
    while stack:
        tmp = stack.pop()
        ans += N_list[tmp][2]
        if N_list[tmp][3][1]:
            stack.append(N_list[tmp][3][1])
        elif N_list[tmp][3][0]:
            stack.append(N_list[tmp][3][0])
    print(f'#{tc} {ans}')