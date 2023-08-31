def solution(strings, n):
    tmp = [[] for _ in range(26)]
    for s in strings:
        tmp[ord(s[n])-96].append(s)
    
    answer = []
    for i in tmp:
        answer += sorted(i)
    return answer