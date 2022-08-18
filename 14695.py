'''
3
3
1 0 0
0 1 0
0 0 1
4
0 0 0
-1 0 -100
342315 0 234234
5 0 15
4
0 1 0
-1 0 -100
342315 0 234234
5 0 15

'''
for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    print(N_list)
    N_distance_list = []
    y_cnt = -1
    for i in N_list:
        y_cnt += 1
        x_cnt = -1
        for j in N_list:
            x_cnt += 1
            N_distance_list[y_cnt][x_cnt] = ((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2 + (j[2] - i[2]) ** 2) ** 0.5

        print(N_distance_list)