ans_list = []
for _ in range(10):
    N_div = int(input()) % 42
    ans_list.append(N_div)
else:
    ans = len(set(ans_list))
print(ans)