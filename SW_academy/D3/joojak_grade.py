for test in range(1, int(input()) + 1):
    NK = list(map(int, input().split(" ")))
    N, K = NK[0], NK[1]
    num = list(map(int, input().split(" ")))
    S = 0
    for i in range(K):
        S += max(num)
        num.pop(num.index(max(num)))
    print(f'#{test}', S)