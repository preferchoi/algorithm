for tc in range(1, 1 + int(input())):
    N = int(input())
    stack = []
    under_line = []
    print(f'#{tc}')
    for i in range(1, 1 + N):
        if i == 1:
            stack = [1]
            print(stack[0])
        else:
            for j in range(i):
                if not under_line:
                    pre = stack.pop()
                    under_line.append(pre)

                elif not stack:
                    under_line.append(pre)

                else:
                    tmp = stack.pop()
                    under_line.append(tmp + pre)
                    pre = tmp
            stack = under_line
            for s in stack:
                print(s, end=' ')
            print()
            under_line = []
