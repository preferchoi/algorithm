def solution(numbers, target):
    answer = 0
    
    for i in range(1<<len(numbers)):
        tmp = 0
        for j in range(len(numbers)):
            if i & (1 << j):
                tmp += numbers[j]
            else:
                tmp -= numbers[j]
        if tmp == target:
            answer += 1    
    return answer