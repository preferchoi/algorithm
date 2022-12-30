mapp = [True] * 1000
# print(mapp)

for i in range(2, len(mapp)):
    if mapp[i]:
        for j in range(i*2, 1000, i):
            mapp[j] = False

key = []
for i in range(len(mapp)):
    if mapp[i]:
        key.append(i)
key = key[2:]
# print(key)
ans = {}
for i in range(6, 1000):
    ans[i] = 0

for i in range(len(key)):
    for j in range(i, len(key)):
        if i + j > 1000:
            continue
        for k in range(j, len(key)):
            if key[i] + key[j] + key[k] < 1000:
                # print(i, j, k)
                ans[key[i]+key[j]+key[k]] += 1

            else:
                break



for tc in range(1, 1 + int(input())):
    print(f'#{tc} {ans[int(input())]}')
