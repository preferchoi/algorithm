key = [True for _ in range(1000001)]
key[0], key[1] = False, False
for i in range(2, 1000001):
    if key[i]:
        cnt = 2
        while i*cnt < 1000001:
            key[i*cnt] = False
            cnt += 1
start_N, end_N = map(int, input().split())

for i in range(start_N, end_N + 1):
    if key[i]:
        print(i)