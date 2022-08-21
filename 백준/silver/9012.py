'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

'''
for tc in range(int(input())):
    stack = []
    s = input()
    for i in s:
        if not stack and i == ')':
            print('NO')
            break
        if i == '(':
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        else:
            print('NO')
            break
    else:
        if stack:
            print('NO')
        else:
            print('YES')