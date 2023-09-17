def solution(k, tangerine):
    answer = 0
    tmp = {}
    for i in tangerine:
        if i in tmp.keys():
            tmp[i] += 1
        else:
            tmp[i] = 1

    tmp = list(tmp.values())
    tmp.sort(reverse=True)
    tmp2 = 0
    for i in tmp:
        tmp2 += i
        answer += 1
        if tmp2 >= k:
            break
    return answer