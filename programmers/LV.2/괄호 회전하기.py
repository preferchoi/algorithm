def is_valid(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or brackets[char] != stack.pop():
                return False
    return not stack

def solution(s):
    count = 0
    for i in range(len(s)):
        if is_valid(s):
            count += 1
        s = s[1:] + s[0]
    return count
