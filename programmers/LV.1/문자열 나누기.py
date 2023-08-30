def solution(s):
    answer, tmp, eq, uneq = 0, '', 0, 0
    for i in s:
        if tmp == '':tmp, eq = i, eq + 1
        else:
            if tmp == i:eq += 1
            else:uneq+=1
        if eq == uneq: tmp, eq, uneq, answer = '', 0, 0, answer+1
    else:
        if tmp != '':answer += 1
    return answer