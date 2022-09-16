'''
1
8 3
0 0 0 0 0 1 0 0
0 1 0 1 0 0 0 1
0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0
0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0
1 0 0 0 0 0 0 0

'''


dic = {}
for i in range(1, 41):
    dic[i] = i**2 + (i-1)**2
print(dic)
for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
