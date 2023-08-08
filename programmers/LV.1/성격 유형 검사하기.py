def solution(survey, choices):
    answer = ''
    mbti = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    for i in range(len(survey)):
        tmp = choices[i] - 4
        if tmp < 0:
            mbti[survey[i][0]] -= tmp
        else:
            mbti[survey[i][1]] += tmp
    
    answer += 'R' if mbti['R'] >= mbti['T'] else 'T'
    answer += 'C' if mbti['C'] >= mbti['F'] else 'F'
    answer += 'J' if mbti['J'] >= mbti['M'] else 'M'
    answer += 'A' if mbti['A'] >= mbti['N'] else 'N'
    
    return answer