'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

'''
for tc in range(1, 1 + int(input())):
    s = input()
    stack = []
    switch = True

    for i in s:
        if i in ['{', '(']:
            stack.append(i)

        if i == '}':
            if not stack:
                switch = False
                break
            elif stack.pop() != '{':
                switch = False
                break
        elif i == ')':
            if not stack:
                switch = False
                break
            elif stack.pop() != '(':
                switch = False
                break

    if stack:
        switch = False

    if switch:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

