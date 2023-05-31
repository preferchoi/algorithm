for test in range(1, int(input())+1):
    array = []
    for i in range(5):
        array.append(list(map(str, input())))
    Max = 0
    for i in range(4):
        print('i:', i)
        if len(array[Max]) < len(array[i+1]):
            Max = i+1
    print(f'#{test}', end=" ")
    for i in range(len(array[Max])):
        for j in range(5):
            if i >= len(array[j]):
                continue
            print(array[j][i], end="")
    print()