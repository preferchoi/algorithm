vect = [3, 5, 1, 1, 2, 3, 2]
arr = [4, 1, 2, 3]

ans_list = []
for i in range(len(arr)):  # 0 -> 1 -> 2 -> 3
    cnt = 0
    for j in range(len(vect)):  # 0 -> 1 -> 2 -> 3 ... -> len(vect) - 1
        if arr[i] == vect[j]:
            cnt += 1
    ans_list.append(cnt)
    print(f'{arr[i]}={cnt}개')

# for i in range(len(arr)):
#     print(arr[i], ans_list[i])

ans_list = []
for i in arr:  # 4 -> 1 -> 2 -> 3
    cnt = 0
    for j in vect:  # 3 -> 5 -> 1 -> 1 -> 2 -> 3 -> 2
        if i == j:
            cnt += 1
    ans_list.append(cnt)
    print(f'{i}={cnt}개')

for i in range(len(arr)):
    print(arr[i], ans_list[i])

ans_list = []
for i in arr:  # 4 -> 1 -> 2 -> 3
    cnt = 0
    for j in vect:  # 3 -> 5 -> 1 -> 1 -> 2 -> 3 -> 2
        if i == j:
            cnt += 1
    ans_list.append([i, cnt])

for i, j in ans_list:
    print(f'{i}={j}개')
