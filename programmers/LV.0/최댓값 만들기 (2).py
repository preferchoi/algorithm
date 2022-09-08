def solution(numbers):
    
    numbers2 = numbers.copy()
    answer1 = max(numbers2)
    numbers2.pop(numbers2.index(answer1))
    answer1 *= max(numbers2)
    
    answer2 = min(numbers)
    numbers.pop(numbers.index(answer2))
    answer2 *= min(numbers)
    
    answer = max(answer1, answer2)
    
    return answer