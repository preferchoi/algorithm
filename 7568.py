'''
5
55 185
58 183
88 186
60 175
46 155

'''

N = int(input())

qq = {}
for i in range(N):
    qq[i + 1] = list(map(int, input().split()))

print(qq)

