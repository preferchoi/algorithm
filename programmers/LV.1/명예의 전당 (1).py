def solution(k, score):
    answer = []
    tmp = []
    for i in score:
        tmp.append(i)
        tmp.sort(reverse=True)
        if len(tmp) < k:
            answer.append(tmp[-1])
        else:
            answer.append(tmp[k-1])
    return answer