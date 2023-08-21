def solution(s):
    answer = []

    while s != '1':
        tmp = s.count('1')
        answer.append(len(s) - tmp)

        s = ''
        while tmp:
            s += str(tmp % 2)
            tmp //= 2
        s = s[::-1]

    return len(answer), sum(answer)