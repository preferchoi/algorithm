N = int(input())
ans = list(map(int, input().split()))
M = max(ans)
sumV = 0
for i in ans:
    sumV += i / M * 100
print(sumV/N)
