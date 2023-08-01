mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
def solution(a, b):
    return week[(sum(mon[:a-1]) + b + 4) % 7]