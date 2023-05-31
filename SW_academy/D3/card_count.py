'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01

'''
for test_case in range(1, int(input())+1):
    Q = input()
    Q_list = []
    for i in range(len(Q)//3):
        Q_list.append(Q[3*i:3*i+3])
    Q_list.sort()
    # print(Q_list)
    if len(Q_list) != len(set(Q_list)):
        print(f'#{test_case} ERROR')
        continue
    S, D, H, C = [], [], [], []
    for i in Q_list:
        if i[0] == 'S':
            S.append([i[0], i[1:3]])
        elif i[0] == 'D':
            D.append([i[0], i[1:3]])
        elif i[0] == 'H':
            H.append([i[0], i[1:3]])
        elif i[0] == 'C':
            C.append([i[0], i[1:3]])
    # print(S, D, H, C)
    print(f'#{test_case} {13-len(S)} {13-len(D)} {13-len(H)} {13-len(C)}')