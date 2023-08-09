def solution(s):
    nums_i = list(map(str, range(10)))
    nums_s = {
        'zero':'0', 
        'one':'1', 
        'two':'2', 
        'three':'3', 
        'four':'4',
        'five':'5', 
        'six':'6', 
        'seven':'7', 
        'eight':'8', 
        'nine':'9'}
    answer = ''
    idx = 0
    while idx < len(s):
        if s[idx] in nums_i:
            answer += s[idx]
            idx += 1
            continue
        if s[idx:idx + 3] in nums_s.keys():
            answer += nums_s[s[idx:idx + 3]]
            idx += 3
            continue
        if s[idx:idx + 4] in nums_s.keys():
            answer += nums_s[s[idx:idx + 4]]
            idx += 4
            continue
        if s[idx:idx + 5] in nums_s.keys():
            answer += nums_s[s[idx:idx + 5]]
            idx += 5
            continue
        
    return int(answer)