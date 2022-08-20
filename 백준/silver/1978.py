key = [True for _ in range(1001)]
key[0], key[1] = False, False

N = int(input())
N_list = list(map(int, input().split()))

for i in range(max(N_list)):
    if key[i]:
        cnt = 2
        while i * cnt < 1001:
            key[i*cnt] = False
            cnt += 1

cnt = 0
for i in N_list:
    if key[i]:
        cnt += 1
print(cnt)