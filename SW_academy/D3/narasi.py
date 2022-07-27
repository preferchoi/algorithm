'''
834
42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34 74 65 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 2 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42

'''
for test in range(1, 11):
    N = int(input())
    ary = input().split(" ")
    if ary[len(ary)-1] == '':
        ary.pop(len(ary)-1)
    array = list(map(int, ary))

    for i in range(N, 0, -1):
        array[array.index(max(array))] = array[array.index(max(array))] - 1
        array[array.index(min(array))] = array[array.index(min(array))] + 1

    print(f'#{test}', max(array)-min(array))