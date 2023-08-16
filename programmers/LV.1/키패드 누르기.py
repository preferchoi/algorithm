def solution(numbers, hand):
    answer = ''
    L_hand, R_hand = [3, 0], [3, 2]
    L_key, R_key = [1, 4, 7], [3, 6, 9]
    for target in numbers:
        if target in L_key:
            L_hand = [target//3, 0]
            answer += 'L'
        elif target in R_key:
            R_hand = [target // 3 - 1, 2]
            answer += 'R'
        else:
            if target == 0:
                tmp = [3, 1]
            else:
                tmp = [target // 3, 1]
            L_range, R_range = abs(tmp[0] - L_hand[0]) + abs(tmp[1] - L_hand[1]), abs(tmp[0] - R_hand[0]) + abs(tmp[1] - R_hand[1])
            if L_range > R_range:
                R_hand = tmp
                answer += 'R'
            elif L_range < R_range:
                L_hand = tmp
                answer += 'L'
            else:
                if hand == 'right':
                    R_hand = tmp
                    answer += 'R'
                else:
                    L_hand = tmp
                    answer += 'L'
            print(L_hand, R_hand)

    return answer