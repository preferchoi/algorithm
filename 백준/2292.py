N = int(input())
key = 1
cnt = 1
while key < N:
    key += 6 * cnt
    cnt += 1

print(cnt)