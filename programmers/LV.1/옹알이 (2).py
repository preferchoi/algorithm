def solution(babbling):
    answer = 0
    able_2 = ["ye", "ma"]
    able_3 = ["aya", "woo"]
    
    for i in babbling:
        flag = True
        idx = 0
        tmp = ''
        while idx < len(i):  
            if i[idx:idx + 2] in able_2:
                if tmp == i[idx:idx + 2]:
                    flag = False
                    break
                tmp = i[idx:idx + 2]
                idx += 2
            elif i[idx:idx + 3] in able_3:
                if tmp == i[idx:idx + 3]:
                    flag = False
                    break
                tmp = i[idx:idx + 3]
                idx += 3
            else:
                flag = False
                break
        if flag:
            answer += 1
        
    
    return answer