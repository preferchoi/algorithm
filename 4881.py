'''
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

'''
TC = int(input())
for tc in range(1, 1 + TC):
    N = int(input())
    N_list = []
    for i in range(N):
        N_list.append(list(map(int, input().split())))

    print(N_list)