'''
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

3 4 0
64 64 64 64
64 64 64 64
64 64 64 63
'''
y, x, b = map(int, input().split())
N_list = [list(map(int, input().split())) for _ in range(y)]
total = 0
for i in N_list:
    total += sum(i)
num = set()
for dy in range(y):
    for dx in range(x):
        num.add(N_list[dy][dx])
if min(num) - 1 >= 0:
    num.add(min(num) - 1)
minV = 999
min_num = 0
for i in num:
    sumV = 0
    if i * y * x - total > b:
        continue

    for dy in range(y):
        for dx in range(x):
            tmp = i - N_list[dy][dx]
            if tmp > 0:  # 땅 메우기
                sumV += tmp
            else:  # 땅 파기
                sumV += tmp * -2
            if minV < sumV:
                break
        if minV < sumV:
            sumV = 0
            break
    print(sumV, i)
    if minV > sumV:
        minV = sumV
        min_num = i
print(minV, min_num)
