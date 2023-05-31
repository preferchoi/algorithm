'''
3
4 47FE
5 79E12
8 41DA16CD

'''
dict_16 = {'0': 0, '1': 1, '2': 2,
           '3': 3, '4': 4, '5': 5,
           '6': 6, '7': 7, '8': 8,
           '9': 9, 'A': 10, 'B': 11,
           'C': 12, 'D': 13, 'E': 14,
           'F': 15}

for tc in range(1, 1 + int(input())):
    N, code = input().split()
    ans = ''
    for i in code:
        q = dict_16[str(i)]
        for j in range(3, -1, -1):
            if q & (1 << j):
                ans += '1'
            else:
                ans += '0'
    print(f'#{tc} {ans}')
