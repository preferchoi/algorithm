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

        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')