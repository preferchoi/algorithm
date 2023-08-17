def solution(nums):
    answer1 = len(nums)//2
    answer2 = len(set(nums))
    return answer1 if answer1 < answer2 else answer2