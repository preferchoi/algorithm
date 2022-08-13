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

    oven = [0]*N
    cnt = -1
    while True:
        cnt += 1
        pizza = oven.pop(0)//2
        if pizza == 0:
            oven.append(N_list.pop(0))
        else:
            oven.append(pizza)
        print(oven, N_list)

        if cnt == 10:
            break