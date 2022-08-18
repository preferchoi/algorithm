'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

'''
for tc in range(1, 1 + int(input())):
    s = input()
    stack = []

    for i in s:
        if not stack:
            stack.append(i)
            continue

        elif stack[-1] == i:
            stack.pop()

        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')
