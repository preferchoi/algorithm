def solution(msg):
    answer = []
    tmp = {chr(k):i for k, i in zip(range(ord('A'), ord('Z')+1), range(1,27))}
    
    index = 27
    pre = msg[0]
    for i in msg[1:]:
        pre += i
        if pre not in tmp.keys():
            tmp[pre] = index
            index += 1
            answer.append(tmp[pre[:len(pre)-1]])
            pre = i
    else:
        if pre:
            answer.append(tmp[pre])
            
    return answer