'''
5
1 4
4 3 3 2 1
5 2 4 3 2 1
4 4 3 3 1
4 3 2 1 1
4 2 3 2 1
4 4 3 2 1
3 4 3 2
5 4 4 2 3 1
5 4 2 4 1 3

'''
N = int(input())

for _ in range(N):
    A, *A_List = map(int, input().split())
    B, *B_List = map(int, input().split())
    A_cnt, B_cnt = [0, 0, 0, 0], [0, 0, 0, 0]
    for i in A_List:
        A_cnt[4-i] += 1
    for i in B_List:
        B_cnt[4-i] += 1

    for i in range(4):
        if A_cnt[i] < B_cnt[i]:
            print('B')
            break
        elif A_cnt[i] > B_cnt[i]:
            print('A')
            break
    else:
        print('D')