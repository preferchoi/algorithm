def solution(s):
    answer = []
    maps = {}
    for i, char in enumerate(s):
        if char in maps:
            answer.append(i - maps[char])
        else:
            answer.append(-1)
        
        maps[char] = i

    return answer