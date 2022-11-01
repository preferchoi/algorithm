for test_case in range(1, int(input()) + 1):
    list_1 = []
    count = 0
    for i in range(int(input())):
        list_1.append(list(map(int, input().split(' '))))
    list_1.sort()
    # print(list_1)
    for i in range(len(list_1)):
        for j in range(i, len(list_1)):
            if list_1[i][1] > list_1[j][1] :
                count += 1
    print(f'#{test_case}', count)
