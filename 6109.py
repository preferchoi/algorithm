'''
2
5 up
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
2 down
16 2
0 2

'''
for tc in range(1, 1 + int(input())):
    N, oper = input().split()
    N = int(N)
    lst = [list(map(int, input().split())) for _ in range(N)]
    print(lst, oper)

    if oper in ['up', 'down']:

    for y in range(N - 1):
        for x in range(N):
