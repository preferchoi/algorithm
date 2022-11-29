for test in range(1, int(input())+1):
    N = int(input())
    array = []
    for i in range(N):
        array.append(list(map(int, map(str, input()))))

    num, num2 = N//2, N//2+1
    sum = 0
    for i in range(N):
        for j in range(num, num2):
            sum += array[i][j]
        if i < N//2:
            num -= 1
            num2 += 1
        else:
            num += 1
            num2 -= 1
    print(f'#{test}', sum)