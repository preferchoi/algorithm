'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

'''

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_idx_list = [i for i in range(1, M + 1)]
    oven = [[0, 0] for _ in range(N)]

    while N_list:
        pizza, pizza_idx = oven.pop(0)
        pizza = pizza // 2
        if pizza == 0:
            oven.append([N_list.pop(0), N_idx_list.pop(0)])
        else:
            oven.append([pizza, pizza_idx])
    while oven:
        pizza, pizza_idx = oven.pop(0)
        pizza = pizza // 2
        if pizza != 0:
            oven.append([pizza, pizza_idx])

    print(f'#{tc} {pizza_idx}')
