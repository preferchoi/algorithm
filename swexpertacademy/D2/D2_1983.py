T = int(input())

for test in range(1, T+1):
    NK = input().split(" ")
    N, K = int(NK[0]), int(NK[1])-1

    list = []

    for i in range(N):
        MFS = input().split(" ")
        M, F, S = int(MFS[0]), int(MFS[1]), int(MFS[2])
        T_score = 0.35 * M + 0.45 * F + 0.20 * S
        list.append(T_score)

    list2 = list.copy()
    list2.sort()
    list2.reverse()

    grade = {'A+': list2[0:N//10], 'A0': list2[N//10:N//10*2], 'A-': list2[N//10*2:N//10*3],
             'B+': list2[N//10*3:N//10*4], 'B0': list2[N//10*4:N//10*5], 'B-': list2[N//10*5:N//10*6],
             'C+': list2[N//10*6:N//10*7], 'C0': list2[N//10*7:N//10*8], 'C-': list2[N//10*8:N//10*9],
             'D0': list2[N//10*9:N//10*10]}
    # for i in range(N):
    #    if list[K] == list2[i]:
    #        list[K]

    print(f'#{test}', end=" ")
    if list[K] in grade['A+']:
        print('A+')
    elif list[K] in grade['A0']:
        print('A0')
    elif list[K] in grade['A-']:
        print('A-')
    elif list[K] in grade['B+']:
        print('B+')
    elif list[K] in grade['B0']:
        print('B0')
    elif list[K] in grade['B-']:
        print('B-')
    elif list[K] in grade['C+']:
        print('C+')
    elif list[K] in grade['C0']:
        print('C0')
    elif list[K] in grade['C-']:
        print('C-')
    elif list[K] in grade['D0']:
        print('D0')
    else:
        print('error!!')