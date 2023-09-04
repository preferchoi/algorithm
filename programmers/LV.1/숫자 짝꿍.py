def solution(X, Y):
    answer = []
    X_list, Y_list = sorted(list(X), reverse=True), sorted(list(Y), reverse=True)
    x_idx, y_idx = 0, 0

    while x_idx < len(X_list) and y_idx < len(Y_list):
        if X_list[x_idx] > Y_list[y_idx]:
            x_idx += 1
        elif X_list[x_idx] < Y_list[y_idx]:
            y_idx += 1
        else:
            answer.append(X_list[x_idx])
            x_idx += 1
            y_idx += 1

    return '-1' if not answer else ''.join(answer) if set(answer) != {'0'} else '0'