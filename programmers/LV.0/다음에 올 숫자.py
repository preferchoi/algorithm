def solution(common):
    answer = 0
    key1 = common[1] - common[0]
    key2 = common[2] - common[1]
    if key1 == key2:
        return common[-1] + key1
    else:
        return common[-1] * common[1] // common[0]