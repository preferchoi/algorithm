'''
5
4 0
4 30
4 47
5 31
5 62

0
11110
101111
11111
111110
'''
for t in range(1, int(input())+1):
    NM = list(map(int, input().split(' ')))
    N, M = NM[0], NM[1]
    b = list(bin(M)[2:])
    b.reverse()
    c = 0
    for i in range(N):
        if len(b) < N:
            c = 1
            break
        if b[i] == '0':
            c += 1
    if c != 0:
        print(f'#{t} OFF')
    else:
        print(f'#{t} ON')
