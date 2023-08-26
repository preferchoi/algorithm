def solution(n, m, section):
    answer = 0
    index = -1

    for s in section:
        if index < s:
            answer += 1
            index = s + m - 1

    return answer