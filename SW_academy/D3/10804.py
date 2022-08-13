'''
2
bdppq
qqqqpppbbd

'''
for tc in range(1, 1 + int(input())):
    s = input()
    c = []
    for i in s[::-1]:
        if i == 'q':
            c.append('p')
        elif i == 'p':
            c.append('q')
        elif i == 'b':
            c.append('d')
        elif i == 'd':
            c.append('b')
    print(f'#{tc}', ''.join(c))
