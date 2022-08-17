maxV = 0
max_idx = 0
for i in range(1, 10):
    N = int(input())
    if N > maxV:

        maxV = N
        max_idx = i
print(maxV)
print(max_idx)