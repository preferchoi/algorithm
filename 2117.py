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
    dic[i] = i ** 2 + (i - 1) ** 2
print(dic)

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # outline = N * 2 + (N - 2) * 2
    maxV = 0
    for y in range(N):
        for x in range(N):

            for k in range(N + 1):
                ans = 0
                for if_y in range(y - k, y + k + 1):
                    for if_x in range(x - k, x + k + 1):
                        if 0 <= if_y < N and 0 <= if_x < N:
                            if lst[if_y][if_x] == 1:
                                ans += M

                if ans - dic[k + 1] > maxV:
                    maxV = ans
                    print(maxV, k, y, x)
    print(maxV)
