def solution(n, lost, reserve):
    answer = n - len(lost)  # 체육복을 잃어버린 학생 수를 제외한 전체 학생 수로 시작합니다.
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # 체육복을 잃어버렸지만 여벌 체육복이 있는 학생을 찾아서,
    # 이 학생들은 다른 학생에게 체육복을 빌려주지 않아도 되므로 제외합니다.
    common = lost_set & reserve_set
    lost_set -= common
    reserve_set -= common
    
    # 여벌 체육복이 있는 학생들이 체육복을 빌려줄 수 있는 경우를 찾습니다.
    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
            answer += 1
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
            answer += 1

    return answer