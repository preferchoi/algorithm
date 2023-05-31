'''
3
27
7777
64

'''
cnt = 0
ans = {}
while cnt ** 3 < 10 ** 18:
    cnt += 1
    ans[cnt ** 3] = cnt

for tc in range(1, 1 + int(input())):
    N = int(input())
    print(f'#{tc}', end=' ')
    if N in ans:
        print(ans[N])
    else:
        print(-1)