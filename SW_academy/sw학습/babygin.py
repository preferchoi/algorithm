'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

'''

for test in range(int(input())):
    AB_list = list(map(int, input().split(" ")))
    dict_A = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    dict_B = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    A_list, B_list = [], []
    turn = 0
    ans_print = True

    for i in AB_list:
        if not ans_print:
            break
        if turn % 2 == 0:
            dict_A[i] += 1
            turn += 1

            if 3 in list(dict_A.values()):
                print(f'#{test + 1} 1')
                ans_print = False
                break

            for K in range(1, 9):
                if dict_A[K - 1] != 0 and dict_A[K] != 0 and dict_A[K + 1] != 0:
                    print(f'#{test + 1} 1')
                    ans_print = False
                    break

        elif turn % 2 == 1:
            dict_B[i] += 1
            turn += 1

            if 3 in list(dict_B.values()):
                print(f'#{test + 1} 2')
                ans_print = False
                break

            for K in range(1, 9):
                if dict_B[K - 1] != 0 and dict_B[K] != 0 and dict_B[K + 1] != 0:
                    print(f'#{test + 1} 2')
                    ans_print = False
                    break

    if ans_print:
        print(f'#{test + 1} 0')
