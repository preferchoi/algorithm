def solution(s):
    answer = list()
    for i in s.split(' '):
        tmp = ''
        for j in range(len(i)):
            tmp += i[j].upper() if j == 0 else i[j].lower()
        answer.append(tmp)
    return ' '.join(answer)