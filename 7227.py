'''
│V│=│(x, y)│= x * x + y * y
2
4
6 0
3 3
-7 2
-4 -1
[6,0] -> [3,3][-7,2][-4,-1]
         [3,-3][13,-2][10,1]
[3,3] -> [-7,2][-4,-1]
         [10,1][7,4]
[-7,2] -> [-4,-1]
          [-3,3]


2
-100000 100000
100000 -100000



2
4
6 0
3 3
-7 2
-4 -1
2
-100000 100000
100000 -100000

'''
from pprint import pprint

for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    TF_list = [[False for _ in range(N)] for _ in range(N)]
    pprint(N_list)

    for i in range(N):  # 0 1 2 3
        for j in range(i+1, N):  #
            TF_list[i][j] = [N_list[i][0] - N_list[j][0], N_list[i][1] - N_list[j][1]]
            TF_list[j][i] = [N_list[i][0] - N_list[j][0], N_list[i][1] - N_list[j][1]]

    pprint(TF_list)

    first_love_A = N_list[0]
    first_love_B = N_list[1]

    V = (first_love_A[0] + first_love_B[0]) ** 2 + (first_love_A[1] + first_love_B[1]) ** 2
    print(V)
