A, B, V = map(int, input().split())
ans = (V - B) // (A - B)
if (V - A) % (A - B):
    ans += 1
print(ans)
