

def solution(arr):
    visit = [True] * 101
    visit[0], visit[1] = False, False
    for i in range(len(visit)):
        if visit[i]:
            for j in range(i*2, 101, i):visit[j] = False
    
    keys = [i for i in range(101) if visit[i]]
    golden_key = {key:0 for key in keys}
    
    for i in arr:
        for j in keys:
            if j > i:break
            tmp, cnt = i, 0
            while True:
                if tmp % j == 0:tmp //= j
                else:break
                cnt += 1
            if golden_key[j] < cnt:golden_key[j] = cnt
    
    answer = 1
    for k, v in golden_key.items():
        if v:
            answer *= k ** v

    return answer