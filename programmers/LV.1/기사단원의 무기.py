def solution(number, limit, power):
    answer = 0
    # for i in range(1, number + 1):
        # tmp = len([j for j in range(1,i+1) if i % j == 0])
        # answer += tmp if tmp <= limit else power
    tmp = [1 for _ in range(number+1)]
    tmp[0] = 0
    for i in range(2, number+1):
        for j in range(i, number + 1, i):
            tmp[j] += 1
    
    return sum([i if i <= limit else power for i in tmp ])