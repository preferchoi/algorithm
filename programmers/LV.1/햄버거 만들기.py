def solution(ingredient):
    answer = 0
    tmp = []
    for i in ingredient:
        if len(tmp) < 3:tmp.append(i)
        elif i == 1:
            if tmp[-3:] == [1, 2, 3]:
                for _ in range(3):tmp.pop()
                answer += 1
            else: tmp.append(i)
        else: tmp.append(i)
    return answer