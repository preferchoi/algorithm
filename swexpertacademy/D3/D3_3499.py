import math
for test in range(1, int(input())+1):
    N = int(input())
    N2 = math.ceil(N/2)
    array = input().split(' ')

    array1 = array[:N2]
    array2 = array[N2:]
    # print(array1, array2)

    A_rray = []
    i = 0

    if N%2 == 1:
        while True:
            A_rray.append(array1[i])
            if i == len(array1)-1:
                break
            A_rray.append(array2[i])
            i += 1
    else:
        while True:
            A_rray.append(array1[i])
            A_rray.append(array2[i])
            i += 1
            if i == len(array1):
                break
    print(f'#{test}', end=" ")
    for i in A_rray:
        print(i, end=" ")
    print()