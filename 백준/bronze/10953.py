'''
5
1,1
2,3
3,4
9,8
5,2
'''

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split(','))
    print(N + M)