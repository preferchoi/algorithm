def solution(n):
    answer = 0
    
    key = n - 1
    
    for i in range(2, int(key ** 0.5) + 1):
        if not key % i:
            answer = i
            break
    else:
        answer = key
            
    

    return answer