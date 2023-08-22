def solution(brown, yellow):
    tmp1 = brown + yellow
    tmp2 = brown//2 + 2

    for i in range(1, tmp2):
        if i * (tmp2 - i) == tmp1:
            return tmp2 - i, i
    answer = []
    return answer