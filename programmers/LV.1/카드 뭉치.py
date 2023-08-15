def solution(cards1, cards2, goal):
    answer = 'No'
    
    for i in goal:
        if cards1 and cards2:
            if cards1[0] == i:
                cards1.pop(0)
            elif cards2[0] == i:
                cards2.pop(0)
            else:
                break
            
        elif cards1:
            if cards1[0] == i:
                cards1.pop(0)
            else:
                break
            
        elif cards2:
            if cards2[0] == i:
                cards2.pop(0)
            else:
                break
            
    else:
        answer = 'Yes'
    return answer