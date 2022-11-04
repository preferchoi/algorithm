for test in range(1, int(input()) + 1):
    array = list(map(str, input()))
    array.sort()
    K = len(array)

    while True:
        K -= 1
        count = 0
        if K == 0:
            break
        if array[K] == array[K - 1]:
            array.pop(K)
            array.pop(K - 1)
            K = len(array)
        for i in range(len(array) - 1):
            if array[i] == array[i + 1]:
                count += 1
        if count == len(array):
            break

    print(f'#{test}', end=" ")
    if len(array) == 0:
        print('Good')
    else:
        for i in array:
            print(i, end="")
        print()
