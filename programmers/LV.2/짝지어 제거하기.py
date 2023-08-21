def solution(s):
    answer = -1
    stack = []
    for el in s:
        if stack:
            if stack[-1] == el:
                stack.pop()
            else:
                stack.append(el)
        else:
            stack.append(el)
    return 0 if stack else 1