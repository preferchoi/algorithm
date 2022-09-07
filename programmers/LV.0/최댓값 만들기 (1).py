def solution(numbers):
    
    answer = max(numbers)
    numbers.pop(numbers.index(answer))
    answer *= max(numbers)
    
    return answer