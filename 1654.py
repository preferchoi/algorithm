K, N = map(int, input().split())
K_list = [int(input()) for _ in range(K)]
ans = (sum(K_list) / K) / (N / K)
key = 100000000000
while True:
    while True:
        sumV = 0
        for i in K_list:
            sumV += i // ans
        if sumV <= N:
            ans += key
            break
        ans -= key
    key //= 10
    if key < 1:
        break
print(ans)