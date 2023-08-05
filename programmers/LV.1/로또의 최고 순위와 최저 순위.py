def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    # print(cnt)
    if cnt > 1:
        answer.append(7 - cnt)
    else:
        answer.append(6)
    
    cnt += lottos.count(0)
    if cnt > 1:
        answer.append(7 - cnt)
    else:
        answer.append(6)
    answer.reverse()
    return answer