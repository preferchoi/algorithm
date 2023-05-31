'''
10
10 3
20 5
30 9
40 12
50 12
60 23
70 23
80 32
90 32
100 32

'''
for tc in range(1, 1 + int(input())):
    N, P = map(int, input().split())
    a, b = N // P, N % P
    print(f'#{tc} {a**(P-b) * (a+1)**b}')
