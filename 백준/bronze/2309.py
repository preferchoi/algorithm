N_list = [int(input()) for _ in range(9)]

for i in range(1 << 9):
    tmp = []
    for j in range(9):
        if i & (1 << j):
            tmp.append(N_list[j])
    if len(tmp) == 7:
        if sum(tmp) == 100:
            break
tmp.sort()
for i in tmp:
    print(i)