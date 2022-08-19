def solution(num, k):
    answer = -1
    if str(k) in list(str(num)):
        answer = str(num).index(str(k)) + 1
    return answer