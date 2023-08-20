def solution(s):
    answer = True
    try:
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            else:
                stack.pop()
        if stack:
            return False
        return True
    except:
        return False
    