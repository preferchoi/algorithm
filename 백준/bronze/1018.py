x, y = map(int, input().split())  # x = 10, y = 13

find_W = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
find_B = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

mapp = []
for i in range(x):
    mapp.append(input())

mini = 9999
# print(mapp)

for i in range(x - 8 + 1):  # 10 - 8 = 2번 순회
    for j in range(y - 8 + 1):  # 13 - 8 = 5번 순회
        count = 0

        for k in range(8):  # 8줄 순회해서 문제없는지 find_와 비교
            if mapp[i + k][j:j + 8] != find_W[k]:
                for l in range(8):
                    if mapp[i + k][j + l] != find_W[k][l]:
                        count += 1
        if count < mini:
            mini = count

        count = 0
        for k in range(8):  # 8줄 순회해서 문제없는지 find_와 비교
            if mapp[i + k][j:j + 8] != find_B[k]:
                for l in range(8):
                    if mapp[i + k][j + l] != find_B[k][l]:
                        count += 1

        if count < mini:
            mini = count

print(mini)
