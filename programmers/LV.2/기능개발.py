def solution(progresses, speeds):
    answer = []
    index = 0
    while index < len(progresses):
        tmp = 0
        for i in progresses[index:]:
            if i >= 100:
                tmp += 1
            else: break
        progresses = [p + s for p, s in zip(progresses, speeds)]
        if tmp:
            index += tmp
            answer.append(tmp)
    
    return answer