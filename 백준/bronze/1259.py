'''
121
1231
12421
0
'''
while True:
    N = input()
    if N == '0':
        break
    if N == N[::-1]:
        print('yes')
    else:
        print('no')