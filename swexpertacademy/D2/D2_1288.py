T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    x = N
    list = []
    y = 0
    while True:
        for i in range(len(str(x))-1, -1, -1):
            n = int(x/10**i) # 4321, 321, 21, 1
            n2 = n*10**i # 4000, 300, 20, 1
            x = x-n2 # 321, 21, 1, 0
            list.append(n)
        x = N * (y+1)
        list.sort()
        list2 = set(list)
        if list2 == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
            print("#{}".format(test_case), N*y)
            break
        y = y + 1
