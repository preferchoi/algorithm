from pprint import pprint

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
pprint(N_list)

for i in N_list:
    if i[0] == 6 or i[5] == 6:
        tmp = [i[1], i[2], i[3], i[4]]
    elif i[1] == 6 or i[3] == 6:
        tmp = [i[0], i[2], i[5], i[4]]
    elif i[2] == 6 or i[4] == 6:
        tmp = [i[0], i[1], i[5], i[3]]
    print(tmp)
