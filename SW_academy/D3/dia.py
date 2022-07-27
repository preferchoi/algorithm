T = int(input())

for test_case in range(1, T + 1):
    case = input()
    if len(case) != 0:
        list = [['.'], ['.'], ['#'], ['.'], ['.']]
        for i in case:
            list[0].extend(['.', '#', '.', '.'])
            list[1].extend(['#', '.', '#', '.'])
            list[2].extend(['.', i, '.', '#'])
            list[3].extend(['#', '.', '#', '.'])
            list[4].extend(['.', '#', '.', '.'])

    for i in list:
        for j in range(len(i)):
            print(i[j], end="\t")
        print()