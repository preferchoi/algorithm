'''
24 18

'''

N, M = map(int, input().split())
ans = N*M
while N % M:
    N, M = M, N % M

print(M)
print(ans//M)