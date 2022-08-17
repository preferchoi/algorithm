s = input()
ans_list = [-1 for _ in range(26)]
cnt = 0
for i in s:
    idx = ord(i) - 97
    if ans_list[idx] == -1:
        ans_list[idx] = cnt
    cnt += 1
print(*ans_list)