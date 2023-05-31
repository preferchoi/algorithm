for test in range(1, int(input())+1):
    array = list(map(int, input().split(" ")))

    print(f'#{test}', end=" ")
    if array[0] == array[1]:
        print(array[2])
    elif array[0] == array[2]:
        print(array[1])
    else:
        print(array[0])