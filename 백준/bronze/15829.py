N = int(input())
s = input()
ans = 0
for i in range(N):
    ans += (ord(s[i]) - 96) * 31 ** i
print(ans)
