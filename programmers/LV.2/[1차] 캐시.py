def solution(cacheSize, cities):
    answer = 0
    log = []
    
    if cacheSize == 0:  # cacheSize가 0인 경우를 처리
        return len(cities) * 5

    for v in cities:
        tmp = v.lower()
        if tmp in log:  # cache hit
            answer += 1
            log.remove(tmp)  # LRU를 위해 hit된 아이템을 log에서 제거
        else:  # cache miss
            answer += 5
            if len(log) >= cacheSize:  # cache가 꽉 찬 경우, 가장 오래된 아이템 제거
                log.pop(0)
        log.append(tmp)  # 새로운 아이템을 cache(log)에 추가

    return answer