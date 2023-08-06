def solution(s):
    answer = True
    s = s.lower()

    return True if s.count('p') == s.count('y') else False