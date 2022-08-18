'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
'''
for tc in range(1, 1 + int(input())):
    s = input()
    stack = []
    print(f'#{tc}', end=' ')
    for i in s:
        if i == '{':
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == '}':
            if stack and stack.pop() == '{':
                continue
            print(0)
            break
        elif i == ')':
            if stack and stack.pop() == '(':
                continue
            print(0)
            break
    else:
        if stack:
            print(0)
        else:
            print(1)
