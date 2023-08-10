def solution(N, stages):
    answer = []
    # print(N)
    # print(stages)
    
    stage_list = [0 for _ in range(N + 2)]
    
    for i in stages:
        stage_list[i] += 1
        
    # print(stage_list)
    tmp = []
    now_user = sum(stage_list)
    for i in stage_list:
        if now_user:
            tmp.append(i/now_user)
            now_user -= i
        else:
            tmp.append(0)
    tmp.pop()
    print(tmp)
    
#     maxV = max(tmp)
#     print(tmp.index(maxV))
    tmp_idx = list(range(N+1))
    print(tmp_idx)
    tmp.pop(0)
    tmp_idx.pop(0)
    while tmp:
        maxV = max(tmp)
        idx = tmp.index(maxV)
        tmp.pop(idx)
        answer.append(tmp_idx.pop(idx))

        
    return answer