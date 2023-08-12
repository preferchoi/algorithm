def solution(s):
    answer = []

    for i in s.split(' '):
        tmp = ''
        for j in range(len(i)):
            tmp += i[j].lower() if j % 2 else i[j].upper() 
        answer.append(tmp)
    return ' '.join(answer)