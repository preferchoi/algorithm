def solution(sides):
    a = sides.pop(sides.index(max(sides)))
    if a >= sum(sides):    
        answer = 2
    else:
        answer = 1
    return answer