for test in range(1, int(input())+1):
    array = list(map(str, input()))
    a, b = 1, 1
    for i in array:
        if i == 'R':
            a = a + b
        elif i == 'L':
            b = a + b
    print(f'#{test}', a, b)