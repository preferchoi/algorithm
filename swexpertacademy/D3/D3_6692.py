for test in range(1, int(input())+1):
    N = int(input())
    per = []
    money = []
    for i in range(N):
        array = list(map(float, input().split(" ")))
        per.append(array[0])
        money.append(array[1])
    sum = float(0)
    for i in range(N):
        sum += per[i] * money[i]
    print(f'#{test}', '%.6f' % sum)