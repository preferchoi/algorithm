def solution(d, budget):
    answer = 0
    d.sort()
    sumV = 0
    for i in d:
        if sumV + i > budget:
            return answer
        answer += 1
        sumV += i
    return answer