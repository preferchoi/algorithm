def solution(arr, divisor):
    answer = sorted([el for el in arr if el%divisor == 0])
    return answer if answer else [-1]