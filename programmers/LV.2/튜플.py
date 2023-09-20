def solution(s):
    answer = []
    
    s_arr = s[2:len(s)-2].split('},{')
    tmp = []
    for i in s_arr:
        tmp.append(list(map(int, i.split(','))))
    tmp.sort(key=len)
    
    for i in tmp:
        for j in i:
            if j not in answer:
                answer.append(j)
                break
        
            
    return answer