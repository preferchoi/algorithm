def solution(clothes):
    answer = 1
    tmp_dict = {k:0 for k in set([i[1] for i in clothes])}
    for i in clothes:
        tmp_dict[i[1]] += 1
    for i in tmp_dict.values():
        answer *= (i+1)
    return answer-1