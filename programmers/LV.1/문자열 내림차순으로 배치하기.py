def solution(s):
    answer = ''
    key = list(range(ord('A'), ord('Z') + 1)) + list(range(ord('a'), ord('z') + 1))
    sorting = {k:0 for k in key}
    for i in s:
        sorting[ord(i)] += 1
    for i in key[::-1]:
        answer += sorting[i] * chr(i)
    return answer