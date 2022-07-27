'''
3
1 1
7 3
100 10

'''
for t in range(int(input())):
    N, K = map(float, input().split(" "))
    if N % K == 0:
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} 1')