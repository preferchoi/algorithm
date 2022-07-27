'''
6
0
1
10
11
111
359
'''

for test in range(1, int(input())+1):
    N = int(input())
    H, M = N // 30, (N % 30)*2
    print(f'#{test}', H, M)