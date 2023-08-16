def solution(board, moves):
    
    answer = 0
    
    box = [[] for _ in range(len(board[0]))]
    
    for i in board:
        idx = 0
        for j in i:
            if j:
                box[idx].append(j)
            idx += 1

    pop_list = []

    for i in moves:
        if box[i-1]:
            tmp = box[i-1].pop(0)
            if not pop_list:
                pop_list.append(tmp)
            elif pop_list[-1] == tmp:
                answer += 2
                pop_list.pop()
            else:
                pop_list.append(tmp)

    return answer