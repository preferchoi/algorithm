def solution(left, right):
    answer = 0
    tmp = list(range(left, right + 1))
    for i in tmp:
        if i ** 0.5 == int(i ** 0.5):
            answer -= i
        else:
            answer += i
    return answer