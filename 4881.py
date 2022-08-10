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
from pprint import pprint
from itertools import permutations

TC = int(input())
for tc in range(1, 1 + TC):
    N = int(input())
    N_list = []
    sumV_list = []
    for i in range(N):
        listV = list(map(int, input().split()))
        N_list.append(listV)
    # pprint(N_list)
    # print(sumV_list)
    # [[2, 1, 2],
    #  [5, 8, 5],
    #  [7, 2, 2]]
    # 각 줄 평균 구해서 낮은거부터 구현? - 아닌듯...
    # 그냥 123456789 부터 987654321까지 돌려서 합 중 낮은거 찾는게?
    # 경우의수 9! = 9*8*7*6*5*4*3*2*1 = 362880
    # [0, 1, 2, 3, 4, 5, 6, 7, 8] 까지 들어가야하니까
    go_back = [[True for _ in range(N)] for _ in range(N)]

    hell_yeah = list(permutations(list(range(N)), N))
    mini = 9999
    for i in hell_yeah:
        sumV = 0
        tmp = 0
        # print(i)
        for j in i:
            # print(tmp, j)
            sumV += N_list[tmp][j]
            tmp += 1
        # print(sumV)
        if mini > sumV:
            mini = sumV
    print(f'#{tc} {mini}')
    '''
    자 어케해볼까
    1층부터 9층까지 순회 돌려?
    depth = 1층
    N_list[depth][:] 스택에 넣어
    
    '''
