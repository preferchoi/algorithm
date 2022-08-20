from itertools import combinations

N, K = map(int, input().split())
N_list = list(map(int, input().split()))

maxi = 0
for i in list(combinations(N_list, 3)):
    s_V = sum(i)
    if s_V > K:
        continue
    elif maxi < s_V:
        maxi = s_V
print(maxi)