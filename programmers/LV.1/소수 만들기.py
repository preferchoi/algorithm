from itertools import combinations

def solution(nums):
    answer = 0
    
    tmp = [True for _ in range(3000)]
    tmp[0], tmp[1] = False, False
    
    for i in range(2, int(3000 ** 0.5) + 1):
        if tmp[i]:
            for j in range(i * i, 3000, i):
                tmp[j] = False

    for comb in combinations(nums, 3):
        if tmp[sum(comb)]:
            answer += 1

    
    return answer