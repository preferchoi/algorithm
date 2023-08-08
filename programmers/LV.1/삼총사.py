def solution(number):
    answer = 0

    for i in range(1<<len(number)):
        tmp = []
        for j in range(len(number)):
            if i & (1<<j):
                tmp.append(number[j])
        if len(tmp) == 3 and sum(tmp) == 0:
            answer += 1
    return answer