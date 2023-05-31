N, X, Y, count = 1, 0, 0, 0
dic1, dic2 = {}, {}
while True:
    dic1[N] = X+1, Y+1
    dic2[(X+1, Y+1)] = N
    X -= 1
    Y += 1
    N += 1
    if X < 0 and Y > count:
        count += 1
        X = count
        Y = 0
    if X == 150:
        break

for test in range(1, int(input())+1):
    bec = list(map(int, input().split(" ")))

    bec1 = dic1.get(bec[0])
    bec2 = dic1.get(bec[1])
    X_num = bec1[0] + bec2[0]
    Y_num = bec1[1] + bec2[1]
    print(f'#{test}', dic2.get((X_num, Y_num)))