'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

'''
from pprint import pprint

for tc in range(1, 1 + int(input())):
    N_list = []
    N = int(input())
    for i in range(N):
        N_list.append(list(map(int, input().split())))
    # print(N_list)
    mapp = [[0 for _ in range(10)] for _ in range(10)]
    # pprint(mapp)

    for lst in N_list:
        for x in range(lst[0], lst[2] + 1):
            for y in range(lst[1], lst[3] + 1):
                if mapp[x][y] == 0:
                    mapp[x][y] = lst[4]
                elif mapp[x][y] != lst[4] or mapp[x][y] == 3:
                    mapp[x][y] = 3
    count = 0
    for i in mapp:
        for j in i:
            if j == 3:
                count += 1
    print(f'#{tc} {count}')